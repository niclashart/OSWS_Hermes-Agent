---
id: arxiv-2610.36169
title: "Don't Pick a Winner: Knowledge Conflicts Need a Prior, Not a Rule"
authors: [(abstract only; authors not fetched)]
year: 2026
score: 7
rubric: {A: 2, B: 1, C: 1, D: 2, E: 1}
axis: [New-Techniques]
status: screened
screened: 2026-10-28
source: https://arxiv.org/abs/2610.36169
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.36169/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.36169/summary.md
tags: [rag-radar, New-Techniques]
---
# Don't Pick a Winner: Knowledge Conflicts Need a Prior, Not a Rule

**Axis:** [[New-Techniques]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2610.36169) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.36169/paper.pdf)

## Core idea
In context-vs-parametric-knowledge conflicts, any fixed resolution rule is beaten somewhere; the paper derives a decision-theoretic model showing fixed rules are linear in the share of reliable contexts while the optimum is convex, arguing for an adaptive prior.

## Results
> "the score of any fixed rule is linear in the share of reliable contexts while the best attainable score is convex, so every fixed rule is beaten wherever it is not exactly optimal" (Abstract)

## Rubric
A 2 · B 1 · C 1 · D 2 · E 1 — Self-reflective conflict-handling technique; empirical scope unclear from abstract; no code evident; lightweight scoring runs anywhere; conflict arbitration needs a new component.

## Relevance for RAG-NIMBF
Not expressible today — graph/conflict-handling technique; weekly fit check should produce `new-axis.md`.

## Status log
- 2026-10-28 screened
