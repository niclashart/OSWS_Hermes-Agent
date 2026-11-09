---
id: arxiv-2611.02550
title: "Re$^3$Rank: Listwise Reranking with Reasoning-Conditioned Retrieval Heads"
authors: [et al.]
year: 2026
score: 9
rubric: {A: 2, B: 2, C: 2, D: 2, E: 1}
axis: [Reranking]
status: fit
screened: 2026-11-04
source: https://arxiv.org/abs/2611.02550
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.02550/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.02550/summary.md
tags: [rag-radar, Reranking]
---
# Re$^3$Rank: Listwise Reranking with Reasoning-Conditioned Retrieval Heads

**Axis:** [[Reranking]] · **Score:** 9/10 · [arXiv](https://arxiv.org/abs/2611.02550) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.02550/paper.pdf)

## Core idea
Listwise reranker where a generator writes a reasoning trace and a scorer reads relevance from retrieval-head attention using the trace as query; joint training via straight-through estimator; 4B beats strongest baseline by 3.11 NDCG@10, 0.6B beats 32B rerankers.

## Results
> "our 4B variant exceeds the strongest baseline by 3.11 NDCG@10 points on average, and even our 0.6B variant surpasses rerankers with up to 32B parameters."…

## Rubric
A 2 · B 2 · C 2 · D 2 · E 1 — reasoning-conditioned listwise reranking; B=2 nine benchmarks, 11 baselines; C=2 code + HF model weights; D=2 0.6B-4B models; E=1 LLM listwise reranker = new pr

## Relevance for RAG-NIMBF
Candidate for the **Reranking** axis at the weekly fit check.

## Status log
- 2026-11-04 screened
- 2026-11-09 fit check: not expressible — new-axis.md on proposal/2026-W46
