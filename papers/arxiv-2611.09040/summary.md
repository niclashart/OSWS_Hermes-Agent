# MV-IVF: Multi-Vector Retrieval via Multi-Vector Clustering

- arXiv: https://arxiv.org/abs/2611.09040
- Score: 8/10 · Axis: Retrieval · Verified: yes (export.arxiv.org, title match)

## Core idea
Builds a native IVF-style inverted-file index directly over multi-vector (point-cloud) document representations instead of proxy/filter-then-rerank pipelines. Key primitive is MV-Lloyd, Lloyd-style clustering of point clouds under a Chamfer objective; queries do best-first beam search over a tree of center point clouds, accelerated with low-bit quantization and query compression. Implemented in MVSIC, a C++ library also containing SVH, MUVERA, MV-Vamana.

## Key results (verbatim)
> "At $90\%$ Recall-$10$@$10$, MV-IVF achieves up to $8.03\times$ lower single-query latency and up to $173.5\times$ higher QPS than the baselines" (Abstract)

> "Across BEIR and LoTTE text retrieval benchmarks, MV-IVF achieves strong latency--recall tradeoffs, the best batched throughput frontiers, and favorable build-time and index-size profiles." (Abstract)

> "MV-Vamana is highly competitive in the single-query regime, although its construction is substantially more expensive." (Sec. 1)

No public code release is stated in the paper (MVSIC availability unclear).

## Rubric
A 2 · B 2 · C 1 · D 1 · E 1 — A: late-interaction/multi-vector retrieval, a clear new option; B: 8 BEIR datasets + LoTTE against strong baselines; C: no stated open release of MVSIC; D: optimized C++, ColBERTv2 embeddings, feasibility on consumer hardware unclear; E: late-interaction retrieval = new provider, not a config value today.

## Affected axis
Retrieval — a `retrieval_strategy` value for multi-vector/late-interaction would be needed (currently not expressible; ColBERT-style = new provider).

## Status log
- 2026-11-09 screened
