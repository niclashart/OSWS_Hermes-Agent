#!/opt/hermes/.venv/bin/python3
"""RAG Radar collector (Hermes cron pre-script, no LLM).

Pulls the repo, queries arXiv, Semantic Scholar, GitHub releases and new HF embedders/rerankers, dedups against
state/seen.json and appends new items to state/inbox.jsonl.
Stdout is injected into the agent prompt; if nothing is pending it prints
{"wakeAgent": false} so the LLM run is skipped. Every run is logged to state/runs.jsonl.
"""
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

REPO = os.environ.get("RADAR_REPO", "/opt/data/osws")
SEEN = os.path.join(REPO, "state", "seen.json")
INBOX = os.path.join(REPO, "state", "inbox.jsonl")
RUNS = os.path.join(REPO, "state", "runs.jsonl")  # one line per run, read by radar-metrics.py
UA = {"User-Agent": "rag-radar/1.0 (research monitoring)"}

ARXIV_QUERY = (
    '(cat:cs.IR OR cat:cs.CL) AND (abs:"retrieval-augmented" OR abs:"retrieval augmented" '
    'OR abs:RAG OR abs:reranker OR abs:reranking OR abs:chunking)'
)
# Semantic Scholar paper IDs whose new citers we track (RAGAS, ARES).
S2_SEEDS = {"RAGAS": "arXiv:2309.15217", "ARES": "arXiv:2311.09476"}
S2_CUTOFF = time.strftime("%Y-%m-%d", time.gmtime(time.time() - 60 * 86400))
GH_REPOS = [
    "langchain-ai/langchain",
    "chroma-core/chroma",
    "lancedb/lancedb",
    "explodinggradients/ragas",
    "UKPLab/sentence-transformers",
    "ollama/ollama",
]


def get(url, timeout=60, retries=3):
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == retries - 1:
                raise
            time.sleep(10 * (attempt + 1))


def arxiv_items():
    q = urllib.parse.quote(ARXIV_QUERY)
    url = (
        "https://export.arxiv.org/api/query?search_query="
        f"{q}&sortBy=submittedDate&sortOrder=descending&max_results=100"
    )
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(get(url))
    for e in root.findall("a:entry", ns):
        aid = e.find("a:id", ns).text.rsplit("/abs/", 1)[-1].rsplit("v", 1)[0]
        yield {
            "id": f"arxiv-{aid}",
            "source": "arxiv",
            "title": " ".join(e.find("a:title", ns).text.split()),
            "abstract": " ".join(e.find("a:summary", ns).text.split()),
            "url": f"https://arxiv.org/abs/{aid}",
            "published": e.find("a:published", ns).text[:10],
        }


def s2_items():
    for seed_name, seed in S2_SEEDS.items():
        url = (
            f"https://api.semanticscholar.org/graph/v1/paper/{seed}/citations"
            "?fields=title,abstract,externalIds,publicationDate&limit=100"
        )
        try:
            data = json.loads(get(url))
        except Exception as exc:  # rate limits are common without API key
            print(f"warn: semantic scholar {seed_name}: {exc}", file=sys.stderr)
            continue
        for row in data.get("data", []):
            p = row.get("citingPaper") or {}
            arx = (p.get("externalIds") or {}).get("ArXiv")
            if not arx or not p.get("title"):
                continue  # only arXiv-backed papers: verifiable + open access
            if (p.get("publicationDate") or "") < S2_CUTOFF:
                continue  # citation list is not sorted by date; skip old citers
            yield {
                "id": f"arxiv-{arx}",
                "source": f"s2-citer:{seed_name}",
                "title": p["title"],
                "abstract": p.get("abstract") or "",
                "url": f"https://arxiv.org/abs/{arx}",
                "published": p.get("publicationDate") or "",
            }
        time.sleep(3)


def github_items():
    for repo in GH_REPOS:
        try:
            rel = json.loads(get(f"https://api.github.com/repos/{repo}/releases?per_page=5"))
        except Exception as exc:
            print(f"warn: github {repo}: {exc}", file=sys.stderr)
            continue
        for r in rel:
            if r.get("draft") or r.get("prerelease"):
                continue
            yield {
                "id": f"gh-{repo.replace('/', '_')}-{r['tag_name']}",
                "source": "github-release",
                "title": f"{repo} {r['tag_name']}",
                "abstract": (r.get("body") or "")[:2000],
                "url": r["html_url"],
                "published": (r.get("published_at") or "")[:10],
            }


# HF Hub pipeline tags whose new models map to a RAG-NIMBF slot (see reference/nimbf-capabilities.md).
HF_KINDS = {
    "sentence-similarity": ("embedder", "embedding_models"),
    "text-ranking": ("reranker", "reranker_models"),
}
MTEB_RESULTS = "embeddings-benchmark/results"
HF_MAX_AGE_DAYS = 60
HF_MAX_PARAMS = 12e9  # ~24 GB VRAM in BF16 (rubric D)
QUANT_MARKERS = ("gguf", "awq", "gptq", "mlx", "onnx", "int4", "int8", "fp8", "exl2")


def _keep_model(m, cutoff):
    if (m.get("createdAt") or "")[:10] < cutoff:
        return False
    if m.get("likes", 0) < 5 and m.get("downloads", 0) < 1000:
        return False
    tags = [t.lower() for t in m.get("tags") or []]
    if any(t.startswith("base_model:quantized:") for t in tags) or any(
        q in tags or q in m["id"].lower() for q in QUANT_MARKERS
    ):
        return False  # quantised re-uploads duplicate the original model
    params = (m.get("safetensors") or {}).get("total")
    return not params or params <= HF_MAX_PARAMS


def hf_model_items(fetch=get, today=None, seen=()):
    """New trending embedders/rerankers on the HF Hub (leaderboard watch)."""
    today = today or time.strftime("%Y-%m-%d", time.gmtime())
    cutoff = time.strftime(
        "%Y-%m-%d", time.gmtime(time.mktime(time.strptime(today, "%Y-%m-%d")) - HF_MAX_AGE_DAYS * 86400)
    )
    for tag, (kind, yaml_key) in HF_KINDS.items():
        url = (
            f"https://huggingface.co/api/models?pipeline_tag={tag}&sort=trendingScore&limit=50"
            "&expand[]=createdAt&expand[]=likes&expand[]=downloads&expand[]=safetensors"
            "&expand[]=tags&expand[]=cardData&expand[]=library_name"
        )
        for m in json.loads(fetch(url)):
            if f"hf-{m['id'].replace('/', '_')}" in seen or not _keep_model(m, cutoff):
                continue
            mid = m["id"]
            params = (m.get("safetensors") or {}).get("total")
            if not params:
                size = "size unknown"
            elif params < 1e9:
                size = f"{params / 1e6:.0f}M params"
            else:
                size = f"{params / 1e9:.1f}B params"
            license_ = (m.get("cardData") or {}).get("license") or "no license"
            try:
                card = fetch(f"https://huggingface.co/{mid}/raw/main/README.md").decode("utf-8", "replace")
            except Exception:
                card = ""
            mteb_name = mid.replace("/", "__")
            try:
                fetch(f"https://api.github.com/repos/{MTEB_RESULTS}/contents/results/{mteb_name}")
                mteb = f"https://github.com/{MTEB_RESULTS}/tree/main/results/{mteb_name}"
            except urllib.error.HTTPError:
                mteb = ""
            yield {
                "id": f"hf-{mid.replace('/', '_')}",
                "source": f"hf-model:{kind}",
                "title": f"{mid} (new {kind}, {size}, {license_})",
                "abstract": card[:3000],
                "url": f"https://huggingface.co/{mid}",
                "published": (m.get("createdAt") or "")[:10],
                "slot": f"{yaml_key}: huggingface:{mid}",
                "mteb": mteb,
            }


def main():
    subprocess.run(["git", "-C", REPO, "pull", "-q", "--rebase", "--autostash"], check=True)
    seen = set(json.load(open(SEEN))) if os.path.exists(SEEN) else set()
    first_run = not seen

    def hf_items():
        return hf_model_items(seen=seen)

    new = []
    for gen in (arxiv_items, s2_items, github_items, hf_items):
        try:
            for item in gen():
                if item["id"] in seen:
                    continue
                seen.add(item["id"])
                new.append(item)
        except Exception as exc:
            print(f"warn: {gen.__name__}: {exc}", file=sys.stderr)

    if first_run:
        # Bootstrap: mark backlog as seen, only screen the newest arXiv batch.
        new = [i for i in new if i["source"] == "arxiv"][:30]

    with open(INBOX, "a") as f:
        for item in new:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    with open(SEEN, "w") as f:
        json.dump(sorted(seen), f, indent=0)

    pending = sum(1 for line in open(INBOX) if line.strip())
    with open(RUNS, "a") as f:
        run = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "new": len(new),
               "pending": pending, "woke": pending > 0}
        f.write(json.dumps(run) + "\n")
    if pending == 0:
        print(json.dumps({"wakeAgent": False}))
        return
    print(f"RAG Radar: {len(new)} new, {pending} pending items in {INBOX}.")


if __name__ == "__main__":
    main()
