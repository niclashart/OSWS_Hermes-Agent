#!/opt/hermes/.venv/bin/python3
"""RAG Radar implementation check (Hermes cron pre-script of radar-impl, no LLM).

Selects this week's "very useful" papers from the vault (score >= 8, or status `fit`),
refreshes shallow mirrors of the target repos in .cache/repos/ and prints a snapshot of
their current state (RAG-NIMBF: main only; Enterprise_RAG_Blueprint: all branches),
so the agent can check whether a technique already exists before proposing code.
Stdout is injected into the radar-impl prompt; prints {"wakeAgent": false} if there
are no candidates.
"""
import datetime as dt
import glob
import json
import os
import re
import subprocess

REPO = os.environ.get("RADAR_REPO", "/opt/data/osws")
CACHE = os.path.join(REPO, ".cache", "repos")
DAYS = int(os.environ.get("RADAR_IMPL_DAYS", "7"))
MIN_SCORE = 8
MAX_CANDIDATES = 5
TARGETS = {
    # name: (clone url, refs to inspect; None = all branches)
    "RAG-NIMBF": ("https://github.com/aiengineeringblueprints/RAG-NIMBF.git", ["main"]),
    "Enterprise_RAG_Blueprint": (
        "https://github.com/aiengineeringblueprints/Enterprise_RAG_Blueprint.git", None),
}
# Noise that says nothing about capabilities (logs, checkpoints, binary docs).
SKIP = re.compile(r"(^|/)(\.claude|\.scratch|benchmark_checkpoints|results?|__pycache__)/|\.(pdf|png|jpg|json|csv|lock)$")
SOURCE = re.compile(r"\.(py|ts|tsx|js|j2|ya?ml|toml|sh)$|(^|/)(Dockerfile|README\.md|docker-compose[^/]*)$")


def git(*args, repo=REPO):
    return subprocess.run(
        ["git", "-C", repo, *args], check=True, capture_output=True, text=True
    ).stdout


def frontmatter(path):
    meta = {}
    with open(path) as f:
        if f.readline().strip() != "---":
            return meta
        for line in f:
            if line.strip() == "---":
                break
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip('"')
    return meta


def handled_ids():
    """Paper IDs that already got an implementation check (impl/* branches or main)."""
    ids = set()
    refs = ["origin/main"] + git(
        "for-each-ref", "--format=%(refname:short)", "refs/remotes/origin/impl/").split()
    for ref in refs:
        for path in git("ls-tree", "-r", "--name-only", ref, "--", "implementations").split():
            # implementations/<YYYY-Www>/<id>.md
            ids.add(os.path.basename(path).removesuffix(".md"))
    return ids


def candidates():
    since = dt.date.today() - dt.timedelta(days=DAYS)
    done = handled_ids()
    out = []
    for path in glob.glob(os.path.join(REPO, "vault", "Papers", "*.md")):
        m = frontmatter(path)
        pid = os.path.basename(path).removesuffix(".md")
        try:
            screened = dt.date.fromisoformat(m.get("screened", ""))
            score = int(m.get("score", "0"))
        except ValueError:
            continue
        status = m.get("status", "")
        if screened < since or status == "rejected" or pid in done:
            continue
        if score >= MIN_SCORE or status == "fit":
            summary = next(
                (p for p in (f"papers/{pid}/summary.md", f"papers/arxiv-{pid}/summary.md")
                 if os.path.exists(os.path.join(REPO, p))), "n/a")
            out.append((score, pid, status, m.get("axis", ""), m.get("title", ""), summary))
    out.sort(reverse=True)
    return out[:MAX_CANDIDATES]


def mirror(name, url):
    path = os.path.join(CACHE, name)
    if not os.path.isdir(path):
        os.makedirs(CACHE, exist_ok=True)
        subprocess.run(
            ["git", "clone", "-q", "--bare", "--depth", "1", "--no-single-branch",
             "--filter=blob:limit=1m", url, path], check=True, capture_output=True)
    git("fetch", "-q", "--prune", "--depth", "1", "origin",
        "+refs/heads/*:refs/heads/*", repo=path)
    return path


def tree(path, ref, limit=200):
    files = [f for f in git("ls-tree", "-r", "--name-only", ref, repo=path).split("\n")
             if f and SOURCE.search(f) and not SKIP.search(f)]
    lines = files[:limit]
    if len(files) > limit:
        lines.append(f"... {len(files) - limit} more")
    return lines


def snapshot(name, url, refs):
    path = mirror(name, url)
    heads = git("for-each-ref", "--format=%(refname:short)", "refs/heads", repo=path).split()
    refs = refs or ["main"] + sorted(h for h in heads if h != "main")
    print(f"\n### {name} (`.cache/repos/{name}`)")
    for ref in refs:
        info = git("log", "-1", "--format=%h %ad %s", "--date=short", ref, repo=path).strip()
        print(f"\n#### `{ref}` — {info}")
        if ref == "main":
            print("Source files:")
            print("\n".join(f"- {f}" for f in tree(path, ref)))
        else:
            # Shallow mirror has no merge base: compare trees directly.
            diff = git("diff", "--name-status", "main", ref, repo=path).strip().split("\n")
            diff = [d for d in diff if d and not SKIP.search(d)]
            print(f"Files differing from main ({len(diff)}):")
            print("\n".join(f"- {d}" for d in diff[:80]))


def main():
    git("pull", "-q", "--rebase", "--autostash")
    git("fetch", "-q", "--prune", "origin")
    cands = candidates()
    if not cands:
        print(json.dumps({"wakeAgent": False}))
        return
    y, w, _ = dt.date.today().isocalendar()
    print(f"RAG Radar implementation check {y}-W{w:02d} (papers screened in the last {DAYS} days).")
    print("\n## Candidates (score | id | status | axis | title | summary)")
    for score, pid, status, axis, title, summary in cands:
        print(f"- {score} | {pid} | {status} | {axis} | {title} | {summary}")
    print("\n## Current repository state (mirrors refreshed just now)")
    for name, (url, refs) in TARGETS.items():
        try:
            snapshot(name, url, refs)
        except subprocess.CalledProcessError as e:
            print(f"\n### {name}: mirror failed ({(e.stderr or '').strip()[:200]})")
            print("Do not propose changes for this repository in this run.")


if __name__ == "__main__":
    main()
