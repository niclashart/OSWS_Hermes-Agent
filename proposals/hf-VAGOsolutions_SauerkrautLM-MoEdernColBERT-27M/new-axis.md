# New-axis proposal — hf-VAGOsolutions/SauerkrautLM-MoEdernColBERT-27M

**Model:** VAGOsolutions/SauerkrautLM-MoEdernColBERT-27M (HF) — vault note [[hf-VAGOsolutions_SauerkrautLM-MoEdernColBERT-27M]], screened 2026-11-01, score 8/10. (The 115M sibling shares the same gap.)

## What the model shows
27M-param (12.3M active) multilingual late-interaction (ColBERT-style) retriever, apache-2.0. Quotes (model card): "German retrieval ahead of models up to 22× larger. MKQA de→en 0.690 vs. 0.671 for Qwen3-Embedding-0.6B." and "4.3× the throughput of granite-97m-multilingual-r2 and 47× that of Qwen3-Embedding-0.6B: 6,708 documents per second on one GPU."

## Why not expressible in RAG-NIMBF today
RAG-NIMBF's Embedding axis supports only single-vector dense embedders (`huggingface:<id>` via sentence-transformers). This model returns one multi-vector token-level representation per document; retrieval needs MaxSim late-interaction scoring, which neither `benchmark/retrieval.py` nor the vector-store backends (chroma, lancedb) implement. `embedding_models: huggingface:VAGOsolutions/SauerkrautLM-MoEdernColBERT-27M` would silently load it wrong (if at all).

## What RAG-NIMBF would need
- New embedding provider kind `late-interaction` beside `dense`: wraps a ColBERT-style model (e.g. via `pylate` or RAGatouille, both MIT/Apache) with `encode_documents` / `encode_queries`.
- Retrieval path: multi-vector index (MaxSim) — either a native in-memory MaxSim searcher or a backend extension (LanceDB has multi-vector support); `retrieval_top_k` semantics carry over unchanged.
- Config key: `embedding_kind: dense | late-interaction` (or inferred from the model id), keeping `embedding_models` as the single model slot.

## Estimated effort
Medium (~1–2 weeks): the model slot and metrics stay unchanged; work is the provider, the MaxSim scoring path, index lifecycle, and tests. High value: the model is German-strong at 1/22 the size of current defaults — directly relevant to the German-language Enterprise_RAG_Blueprint context.
