# New-axis proposal — arXiv:2611.09040

**Paper:** "MV-IVF: Multi-Vector Retrieval via Multi-Vector Clustering" (arXiv:2611.09040) — vault note [[arxiv-2611.09040]], screened 2026-11-09, score 8/10.

## What the paper shows
Native IVF-style inverted-file index built directly over multi-vector (point-cloud) document representations; key primitive is MV-Lloyd, Lloyd-style clustering of point clouds under a Chamfer objective. Quote (Abstract): "At $90\%$ Recall-$10$@$10$, MV-IVF achieves up to $8.03\times$ lower single-query latency and up to $173.5\times$ higher QPS than the baselines."

## Why not expressible in RAG-NIMBF today
Multi-vector retrieval is not expressible: `embedding_models` is a single-vector slot and `retrieval_strategy` offers only `similarity`/`mmr` over one vector per chunk. There is no MaxSim/Chamfer scoring path and no multi-vector index backend (`vector_db_backend`: chroma/lancedb only, single-vector).

## What RAG-NIMBF would need
- Embedding provider kind `multi-vector` (one document → list of vectors) beside `dense`; `retrieval_strategy` value `maxsim` (or `chamfer`).
- Backend extension or in-memory multi-vector index with the existing `retrieval_top_k` semantics; latency/QPS flow into the existing efficiency tracking.
- Note: the paper's MVSIC C++ library has unclear release status — a Python fallback (pylate/ColBERT-style) would be the practical adapter.

## Estimated effort
Large (~2+ weeks): touches embedding providers, retrieval scoring, index lifecycle, and efficiency metrics. High benchmark value (latency-vs-recall is a core RAG-NIMBF trade-off) but the biggest engineering item on this week's list.
