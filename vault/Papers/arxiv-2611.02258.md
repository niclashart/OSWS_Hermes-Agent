---
id: arxiv-2611.02258
title: "Beyond Binary Detection: Type-Aware Hallucination Analysis and Hierarchical Detection in Financial Question Answering"
authors: [Xiongyu Chen, Sizhen Zhu, Zhuoer Wang]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [Evaluation]
status: fit
screened: 2026-11-07
source: https://arxiv.org/abs/2611.02258
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.02258/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.02258/summary.md
tags: [rag-radar, evaluation]
---
# Beyond Binary Detection: Type-Aware Hallucination Analysis in Financial QA

**Axis:** [[Evaluation]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.02258) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.02258/paper.pdf)

## Core idea
Type-level hallucination evaluation on PHANTOM (SEC filings): nine hallucination subtypes, diagnosis of an LLM detector per subtype, and a two-stage hierarchical detector (binary first, then subtype) with an enhanced prompt.

## Results
> "raising binary accuracy to 95.6% and subtype accuracy to 56.1%" (Abstract; Sec. 4.2: reasoning_errors 68.3→94.7); "type-level evaluation exposes detector weaknesses that aggregate metrics conceal" (Abstract).

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — hallucination-subtype metrics go beyond RAGAS faithfulness; new custom metric needed.

## Relevance for RAG-NIMBF
Not expressible today: needs a hallucination-subtype custom metric. Candidate for `new-axis.md`.

## Status log
- 2026-11-07 screened
- 2026-11-09 fit check: not expressible — new-axis.md on proposal/2026-W46
