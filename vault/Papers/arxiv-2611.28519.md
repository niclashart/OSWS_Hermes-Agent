---
id: arxiv-2611.28519
title: "SupportChain: Trace-Calibrated Aggregation of Quote-Grounded Reasoning Chains for Multi-Hop RAG with Small Readers"
authors: [Zhexi Gu]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-11-24
source: https://arxiv.org/abs/2611.28519
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.28519/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.28519/summary.md
tags: [rag-radar, New-Techniques]
---
# SupportChain: Trace-Calibrated Aggregation of Quote-Grounded Reasoning Chains for Multi-Hop RAG with Small Readers

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.28519) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.28519/paper.pdf)

## Core idea
Index-free multi-hop RAG: split the question into hops, bind each hop answer to a quoted sentence, score each execution from its own trace, and merge executions by answer support and pooled reliability with early stopping. 9B reader, no graph index.

## Results
> "With a 9B reader under the HippoRAG~2 protocol, SupportChain reaches 63.0 F1 on MuSiQue, above the best earlier result of 59.2, which used a 20B reader." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 0 — trace-calibrated execution merging needs framework redesign; no NIMBF axis covers it.

## Relevance for RAG-NIMBF
Not expressible: multi-hop orchestration with trace-based merging/early stopping goes beyond `retrieval_multihop`. See [[New-Techniques]].

## Status log
- 2026-11-24 screened
