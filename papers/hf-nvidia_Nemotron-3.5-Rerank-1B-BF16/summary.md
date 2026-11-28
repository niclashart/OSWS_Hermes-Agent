# nvidia/Nemotron-3.5-Rerank-1B-BF16

**Model card:** https://huggingface.co/nvidia/Nemotron-3.5-Rerank-1B-BF16 (HF, 2026-11-13)
**Params:** 1.6B (base: mistralai/Ministral-3-3B-Instruct-2512-BF16) · **License:** OpenMDW-1.1
**Source:** hf-model:reranker · **Ready-to-use slot:** `reranker_models: huggingface:nvidia/Nemotron-3.5-Rerank-1B-BF16`
**mteb link:** none

## Core idea
1B sibling of the already-screened Nemotron-3.5-Rerank-8B: multilingual (34 languages incl. German) and multimodal (text / page image / both) cross-encoder reranker producing a relevance logit. Loadable via sentence-transformers `CrossEncoder`; vLLM supported.

## Key results (verbatim quotes)
> "The reranking model serves as a key component of a multimodal retrieval system, such as a vision RAG pipeline, where it helps improve overall retrieval accuracy." (Description)

> "**Benchmark Score:** NDCG@10" — ViDoRe V3: image 63.50, text 64.66, image+text 64.79; MIRACL-VISION image 72.17. Qwen3-VL-Reranker-2B: 60.86 / 60.11 / 60.58 / 65.25; both reranking top-50 candidates from Nemotron-3.5-Embed-1B-BF16. (Evaluation Dataset)

So the 1B beats Qwen3-VL-Reranker-2B on all four columns (+2.6 to +6.9 NDCG@10) at roughly half the size.

## Rubric
- **A 2** — beats Qwen3-VL-Reranker-2B (a reranker class users run) with public benchmark numbers; 34-language text reranking incl. German.
- **B 2** — NDCG@10 on two benchmarks (ViDoRe V3, MIRACL-VISION) with named baselines.
- **C 1** — OpenMDW-1.1: permissive but not MIT/Apache; weights open.
- **D 2** — 1.6B params, runs on consumer GPU / quantised.
- **E 1** — sentence-transformers `CrossEncoder` loadable for text, but multimodal (page-image) reranking needs a new provider (per rubric note).

**Total: 8/10 → relevant**

## Affected axis
Reranking — text variant pluggable as `huggingface:` CrossEncoder slot; multimodal variant not expressible today (new-axis candidate).

## Status log
- 2026-11-28 screened (HF model: no PDF; summary from model card)
