# New axis proposal — Retrieving Patristic References and Modelling Topics in Bullinger's Reformation Correspondence (arxiv-2611.25247)

- Paper: https://arxiv.org/abs/2611.25247
- Verdict: **not expressible** in RAG-NIMBF today.

## What RAG-NIMBF would need
Hybrid BM25+dense fusion: BM25 94% R@20 on explicit citations, dense 16% on implicit, fusion 22% implicit R@20 close to cross-encoder reranking (26%) without its cost. Explicitly listed as not expressible (internal adapter has no hybrid fusion). Needs: `retrieval_strategy: hybrid` (RRF, keyword+vector weights honoured by the internal adapter, not only managed ones). Effort: M. Strongest new-axis candidate this week.
