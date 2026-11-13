# Active Learning of Approximate LLM Ranking for Energy-Efficient Retrieval of Long Queries

- arXiv/HF id: arxiv-2611.16488
- Score: 7/10 (A 2, B 2, C 1, D 1, E 1)
- Date screened: 2026-11-13
- Axis: Query-Transformation
- Source: https://arxiv.org/abs/2611.16488

## Core idea
LAAM inserts a lightweight learned predictor between semantic retrieval and LLM reranking; an active-learning loop has an LLM label only the most informative documents, exposing a continuous energy–accuracy trade-off.

## Key results (verbatim quotes)
> "For verbose queries, LAAM achieves 87% of average P@10 achieved by DeepSeek's reranking (0.459 vs. 0.526), while requiring only 3.3% of the per-query energy consumption." (Abstract)

## Rubric justification
A 2 · B 2 · C 1 · D 1 · E 1 — clear new efficiency option on the reranking path; strong TREC evaluation with significance tests, but no code released and needs a proprietary LLM (DeepSeek v3); new provider needed in RAG-NIMBF.

## RAG-NIMBF fit
Not expressible today: LLM-reranker approximation with energy budgeting needs a new reranking provider + Efficiency-axis extension (new-axis.md candidate).
