"""Tests for the HF model collector in radar-collect.py (run: pytest scripts/tests)."""
import importlib.util
import json
import pathlib

_spec = importlib.util.spec_from_file_location(
    "radar_collect", pathlib.Path(__file__).parents[1] / "radar-collect.py"
)
rc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rc)

NOW = "2026-10-31"


def model(mid, created="2026-10-20", likes=20, downloads=5000, params=600_000_000,
          tags=("sentence-transformers", "license:apache-2.0"), license="apache-2.0"):
    return {
        "id": mid, "createdAt": f"{created}T00:00:00.000Z", "likes": likes, "downloads": downloads,
        "safetensors": {"total": params} if params else None, "tags": list(tags),
        "library_name": "sentence-transformers", "cardData": {"license": license},
    }


def fake_fetch(listing, readme="# Model card\nMTEB retrieval 61.2", mteb=()):
    """Answers the HF listing, README and MTEB-results URLs like the real services."""
    def fetch(url):
        if "huggingface.co/api/models?" in url:
            tag = "text-ranking" if "text-ranking" in url else "sentence-similarity"
            return json.dumps(listing.get(tag, [])).encode()
        if url.endswith("/README.md"):
            return readme.encode()
        if "embeddings-benchmark/results" in url:
            name = url.rsplit("/", 1)[-1]
            if name in mteb:
                return b"[]"
            raise rc.urllib.error.HTTPError(url, 404, "Not Found", {}, None)
        raise AssertionError(f"unexpected url {url}")
    return fetch


def test_new_embedder_becomes_inbox_item_with_nimbf_slot():
    listing = {"sentence-similarity": [model("acme/embed-small")]}
    items = list(rc.hf_model_items(fake_fetch(listing, mteb={"acme__embed-small"}), today=NOW))
    assert len(items) == 1
    it = items[0]
    assert it["id"] == "hf-acme_embed-small"
    assert it["source"] == "hf-model:embedder"
    assert it["url"] == "https://huggingface.co/acme/embed-small"
    assert it["published"] == "2026-10-20"
    assert it["slot"] == "embedding_models: huggingface:acme/embed-small"
    assert "600M params" in it["title"] and "apache-2.0" in it["title"]
    assert "MTEB retrieval 61.2" in it["abstract"]
    assert it["mteb"] == "https://github.com/embeddings-benchmark/results/tree/main/results/acme__embed-small"


def test_only_fresh_popular_original_models_that_fit_consumer_gpu_are_kept():
    listing = {
        "text-ranking": [
            model("acme/rerank-base"),
            model("old/classic-reranker", created="2025-01-10"),  # older than 60 days
            model("someone/rerank-base-GGUF", tags=("gguf", "base_model:quantized:acme/rerank-base")),
            model("tiny/unknown", likes=1, downloads=50),  # no traction
            model("big/rerank-70b", params=70_000_000_000),  # > 24 GB VRAM even quantised
        ]
    }
    ids = [i["id"] for i in rc.hf_model_items(fake_fetch(listing), today=NOW)]
    assert ids == ["hf-acme_rerank-base"]


def test_already_seen_models_cost_no_extra_requests():
    calls = []
    listing = {"sentence-similarity": [model("acme/embed-small"), model("acme/embed-large")]}
    inner = fake_fetch(listing)

    def counting(url):
        calls.append(url)
        return inner(url)

    items = list(rc.hf_model_items(counting, today=NOW, seen={"hf-acme_embed-small"}))
    assert [i["id"] for i in items] == ["hf-acme_embed-large"]
    assert not any("embed-small" in u for u in calls)
