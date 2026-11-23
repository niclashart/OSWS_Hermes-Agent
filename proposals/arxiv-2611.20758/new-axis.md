# New axis proposal — UniGraph: A Unified Graph-based Index for Dynamic Hybrid Dense-Sparse Vector Retrieval (arxiv-2611.20758)

- Paper: https://arxiv.org/abs/2611.20758
- Verdict: **not expressible** in RAG-NIMBF today.

## What RAG-NIMBF would need
Unified graph index for hybrid dense+sparse retrieval with dynamic updates. RAG-NIMBF `vector_db_backend` supports only chroma/lancedb and the internal adapter has no hybrid BM25+dense fusion. Needs: new vector_db_backend adapter (graph index) plus internal hybrid retrieval (RRF). Effort: L.
