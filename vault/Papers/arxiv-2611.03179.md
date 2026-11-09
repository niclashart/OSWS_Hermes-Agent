---
id: arxiv-2611.03179
title: "Every Clause Counts: Instruction-Following Reranking by Multiplying Small, Answerable Questions"
authors: [et al.]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [Reranking]
status: fit
screened: 2026-11-04
source: https://arxiv.org/abs/2611.03179
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.03179/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.03179/summary.md
tags: [rag-radar, Reranking]
---
# Every Clause Counts: Instruction-Following Reranking by Multiplying Small, Answerable Questions

**Axis:** [[Reranking]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.03179) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.03179/paper.pdf)

## Core idea
DMReranker: zero-shot reranker that splits an instructed query into typed clauses answered by a small judge model; answer probabilities are multiplied into one score, obeying instructions like 'beginners only' without training.

## Results
> "DMReranker reaches a macro WISE of 50.9 over all six InfoSearch dimensions while keeping original-mode nDCG@10 at 82.9."…

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — instruction-conditioned reranking = new Reranking option; B=2 InfoSearch benchmark vs GPT-4o listwise; C=1 no code release mentioned; D=2 small judge model; E=1

## Relevance for RAG-NIMBF
Candidate for the **Reranking** axis at the weekly fit check.

## Status log
- 2026-11-04 screened
- 2026-11-09 fit check: not expressible — new-axis.md on proposal/2026-W46
