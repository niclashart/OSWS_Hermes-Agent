# New-axis proposal — arXiv:2611.03927

**Paper:** "Modular and Efficient Approximate Nearest Neighbors Search with Vectorium and kANNolo" (arXiv:2611.03927) — vault note [[arxiv-2611.03927]], screened 2026-11-04, score 8/10.

## What the paper shows
Two open-source Rust ANN libraries (Vectorium, kANNolo) that factor vector representation, distance, quantizer and index independently; dense/sparse/multi-vector generic. Quote (Abstract): "our Product Quantization matches Faiss in accuracy at competitive speed, our RaBitQ and HNSW match or outperform their reference implementations, and our IVF outperforms Faiss."

## Why not expressible in RAG-NIMBF today
`vector_db_backend` accepts only `chroma` and `lancedb`; both hide the ANN index internals, so quantization, graph type and search parameters are not benchmark-visible axes. There is no pluggable ANN-index slot through which Vectorium/kANNolo could be compared against the backends' defaults on recall/latency/memory.

## What RAG-NIMBF would need
- Config key `vector_index: <backend-default | hnsw | ivf | …>` and `vector_quantization: <none | pq | rabitq | binary>` as first-class axes, either via new backends or a local in-memory ANN adapter.
- Efficiency metrics (QPS at recall targets, index memory) already partially exist via the efficiency stage; a recall@k-vs-latency report per index config would be the benchmark output.

## Estimated effort
Medium (~1–2 weeks): an in-memory ANN adapter with pluggable index/quantizer, plus wiring and tests. Both libraries are open-source Rust with Python bindings, consumer-feasible.
