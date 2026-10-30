# 2610.38683 — Quantum-Inspired Pairwise Ranking Aggregation via Active LLM Feedback

**Score:** 7/10 · **Axis:** Reranking · [arXiv](https://arxiv.org/abs/2610.38683) · [HTML](https://arxiv.org/html/2610.38683)

## Core idea
LLM-IRA fuses rankings from multiple retrievers by asking an LLM pairwise judgments only on high-disagreement pairs; fusion weights are learned interactively and applied as a fast pointwise linear score combination. No full pairwise matrix, no listwise prompting, no training data.

## Key results (verbatim quotes)
> "it already clears the best unsupervised baseline within as few as 5 LLM calls per query" (Abstract (DL19/DL20 profiling))

## Rubric score with justification
A 2 (multi-retriever rank aggregation is a new axis) · B 2 (BEIR + TREC DL, significance tests) · C 1 (judge is open-weight Llama-3.1-8B; code release unclear) · D 2 (8B judge on 24 GB) · E 1 (needs an aggregation component over multiple retriever outputs)

## Affected axis
Reranking: Not expressible: RAG-NIMBF has a single retrieval_strategy. Needs a new axis 'rank_fusion' / multi-retriever ensemble before LLM-IRA could be configured.
