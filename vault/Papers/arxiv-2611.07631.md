---
id: arxiv-2611.07631
title: "MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents"
authors: [Mayank Anand, Subham Raj, Aman Vaibhav Jha, Sriparna Saha]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [New-Techniques]
status: screened
screened: 2026-11-07
source: https://arxiv.org/abs/2611.07631
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.07631/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.07631/summary.md
tags: [rag-radar, new-techniques]
---
# MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.07631) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.07631/paper.pdf)

## Core idea
Training-free agent-memory lifecycle: judge-gated consolidation (LLM ensemble certifies merges as lossless, plus token-coverage and length gates) and retrospective attribution — retrieved memories that supported answers get retrieval-priority updates, with a UCB bonus for under-exposed memories.

## Results
> "the full retrieval stack improves evidence recall@5 by 11.92 percentage points over bare cosine, with confidence-gated feedback adding 1.50 points overall without reference answers or reranker training" (Abstract, Sec. 4)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — memory lifecycle + attribution feedback; new component beyond any existing axis.

## Relevance for RAG-NIMBF
Not expressible: needs a memory axis (consolidation gating, attribution feedback). Candidate for `new-axis.md`.

## Status log
- 2026-11-07 screened
