---
id: arxiv-2611.09040
title: "MV-IVF: Multi-Vector Retrieval via Multi-Vector Clustering"
authors: [Kishen N Gowda, Laxman Dhulipala]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 1, E: 1}
axis: [Retrieval]
status: screened
screened: 2026-11-09
source: https://arxiv.org/abs/2611.09040
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.09040/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.09040/summary.md
tags: [rag-radar, Retrieval, multi-vector]
---
# MV-IVF: Multi-Vector Retrieval via Multi-Vector Clustering

**Axis:** [[Retrieval]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.09040) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.09040/paper.pdf)

## Core idea
Native IVF index over multi-vector point clouds (MV-Lloyd clustering under Chamfer objective); at 90% Recall@10 up to 8x lower latency and 173x higher QPS than proxy-based baselines on BEIR/LoTTE.

## Results
> "At $90\%$ Recall-$10$@$10$, MV-IVF achieves up to $8.03\times$ lower single-query latency and up to $173.5\times$ higher QPS than the baselines" (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 1 · E 1 — strong evaluation; MVSIC release not stated; late-interaction = new provider in RAG-NIMBF.

## Relevance for RAG-NIMBF
Not expressible today: multi-vector retrieval would need a new `retrieval_strategy` value / provider.

## Status log
- 2026-11-09 screened
