# MAPS: Macro-Adaptive Parallel Reasoning for Regulating Search Momentum (arXiv:2610.29792)

## Core idea
Introduces "search momentum" — the accumulated retrieval tendency induced by historical sub-query changes during interleaved reasoning-retrieval. MAPS mitigates query-intent drift by retaining retrieved knowledge and a refined reasoning state, and converts sequential reasoning into parallel reasoning: per iteration it generates complementary sub-queries, retrieves in parallel, and consolidates evidence.

## Results
> "Experiments on six question-answering benchmarks demonstrate that MAPS consistently outperforms representative RAG methods across different backbone models" (Abstract). Evaluated with Cover-EM, top-5 passages, max 10 iterations (Sec. 4). Code: https://github.com/NEUIR/MAPS.

## Rubric
A 2 · B 2 · C 2 · D 2 · E 0 — agentic parallel query decomposition, new RAG technique; 6 benchmarks; open code; consumer-GPU compatible via API/open models; needs a reasoning-loop component RAG-NIMBF lacks.

## Relevance for RAG-NIMBF
Query decomposition / iterative agentic retrieval is explicitly not expressible — needs a new axis (query-decomposition mode, iteration budget).
