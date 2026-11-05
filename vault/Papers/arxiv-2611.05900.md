---
id: arxiv-2611.05900
title: "Weaver: Weaving Preference Evidence through Incremental Reasoning for Personalized Retrieval-Augmented Generation"
authors: [Weaver authors]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 2, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-11-05
source: https://arxiv.org/abs/2611.05900
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.05900/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.05900/summary.md
tags: [rag-radar, New-Techniques]
---
# Weaver (Personalized RAG)

**Axis:** [[New-Techniques]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.05900) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.05900/paper.pdf)

## Core idea
Dual-layer graph (Intent Dependency Graph over Memory-Conditioned Retrieval Trajectories): tracks information gaps, incrementally retrieves missing preference evidence from conversation memory, and resolves complementary/conflicting preferences under temporal-situational scope before answering.

## Results
> "Weaver outperforms leading baselines in both evidence completeness and answer quality" on personalized RAG benchmarks, particularly PersonaMem (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 0 — personalized memory-graph retrieval; PersonaMem vs baselines; code unclear; LLM pipeline feasible; not expressible.

## Relevance for RAG-NIMBF
Personalization and memory-graph reasoning are beyond multi-hop follow-ups; would need a new axis (user memory / personalization).

## Status log
- 2026-11-05 screened
