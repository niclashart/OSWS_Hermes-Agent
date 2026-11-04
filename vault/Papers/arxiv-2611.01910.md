---
id: arxiv-2611.01910
title: "EAGR: Evidence-Guided Adaptive Graph Retrieval"
authors: [et al.]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 2, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-11-04
source: https://arxiv.org/abs/2611.01910
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.01910/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.01910/summary.md
tags: [rag-radar, New-Techniques]
---
# EAGR: Evidence-Guided Adaptive Graph Retrieval

**Axis:** [[New-Techniques]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.01910) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.01910/paper.pdf)

## Core idea
Adaptive multi-hop retrieval over an implicit semantic graph in a plain VectorDB: an LLM assesses accumulated evidence, expands the frontier via metadata neighborhood lookup, and terminates when sufficient — no GraphDB, no query rewriting.

## Results
> "EAGR achieves the highest LLM-based answer accuracy among evaluated methods, outperforming the vanilla RAG by 17% and strongest graph-aware baseline by 4% percentage points averaged across three popular benchmarks HotPotQA, 2WikiMultiHopQA, and MuSiQue."…

## Rubric
A 2 · B 2 · C 1 · D 2 · E 0 — evidence-guided adaptive retrieval loop; B=2 three multi-hop benchmarks; C=1 no code mentioned; D=2 LLM-driven, standard VectorDB; E=0: adaptive frontier-expans

## Relevance for RAG-NIMBF
New technique — not expressible today; candidate for new-axis.md at weekly fit check.

## Status log
- 2026-11-04 screened
