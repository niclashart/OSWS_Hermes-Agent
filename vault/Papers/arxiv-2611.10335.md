---
id: arxiv-2611.10335
title: "Two-Sided Conformal Evidence Sets for Retrieval-Augmented Generation"
authors: [anonymous]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 1, E: 1}
axis: [Evaluation]
status: screened
screened: 2026-11-11
source: https://arxiv.org/abs/2611.10335
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.10335/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.10335/summary.md
tags: [rag-radar, Evaluation]
---
# Two-Sided Conformal Evidence Sets for RAG

**Axis:** [[Evaluation]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.10335) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.10335/paper.pdf)

## Core idea
Separate support and refutation evidence sets with finite-sample coverage guarantees ≥ 1−α per side under exchangeability.

## Results
> "CES closely tracks nominal coverage across α∈{0.05,0.10,0.15,0.20,0.30}, with maximum deviations of 3.0 percentage points for support and 5.4 for refutation" (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 1 · E 1 — calibrated coverage as new evaluation metric; no public code; new post-retrieval component needed.

## Relevance for RAG-NIMBF
Coverage guarantees not expressible → likely `new-axis.md` (Evaluation extension).

## Status log
- 2026-11-11 screened
