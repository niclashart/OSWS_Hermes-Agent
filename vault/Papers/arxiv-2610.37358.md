---
id: arxiv-2610.37358
title: "When Is Additional Retrieval Worthwhile? A Cost-Aware Study of Evidence Gain and Answer Reliability in RAG"
authors: [(abstract only; authors not fetched)]
year: 2026
score: 7
rubric: {A: 2, B: 1, C: 1, D: 2, E: 1}
axis: [Retrieval]
status: screened
screened: 2026-10-28
source: https://arxiv.org/abs/2610.37358
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.37358/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.37358/summary.md
tags: [rag-radar, Retrieval]
---
# When Is Additional Retrieval Worthwhile? A Cost-Aware Study of Evidence Gain and Answer Reliability in RAG

**Axis:** [[Retrieval]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2610.37358) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.37358/paper.pdf)

## Core idea
A cost-aware two-action retrieval policy decides per question between dense-retrieval-plus-reranking and hybrid lexical-dense retrieval, using a regularized linear model trained on pre-routing features and frozen before held-out evaluation.

## Results
> "the policy triggers hybrid retrieval on 46 questions (24.5%) and obtains the same evidence Hit@10 as always-hybrid retrieval (78.70%, versus 76.92% for always-keep)" (Abstract)

## Rubric
A 2 · B 1 · C 1 · D 2 · E 1 — Retrieval routing touches the Retrieval axis; single dataset (QASPER subset) and authors flag weak statistical power; 4-bit Qwen3-4B runs on consumer GPU; hybrid/routing needs a new component.

## Relevance for RAG-NIMBF
Candidate value for `matrix.retrieval_strategy` or a new adapter component; decide in weekly fit check.

## Status log
- 2026-10-28 screened
