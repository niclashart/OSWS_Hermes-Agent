---
id: arxiv-2611.04343
title: "Do Retrieval Ranking Models Capture Event Order? A Study of Timeline-Constrained Retrieval"
authors: [et al.]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 1, E: 1}
axis: [Evaluation]
status: rejected
screened: 2026-11-04
source: https://arxiv.org/abs/2611.04343
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.04343/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.04343/summary.md
tags: [rag-radar, Evaluation]
---
# Do Retrieval Ranking Models Capture Event Order? A Study of Timeline-Constrained Retrieval

**Axis:** [[Evaluation]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.04343) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.04343/paper.pdf)

## Core idea
Timeline-constrained retrieval: dense retrievers and rerankers barely beat lexical retrieval when relevance requires matching an ordered sequence of events; an order-preserving reranking method yields large gains on a new disaster-report collection.

## Results
> "Experiments show that state-of-the-art semantic retrievers and rerankers provide only limited improvements over lexical retrieval, suggesting that their semantic matching capabilities do not reliably capture temporal constraints."…

## Rubric
A 2 · B 2 · C 1 · D 1 · E 1 — new evaluation protocol + collection for order-sensitive retrieval (Evaluation axis); B=2 controlled study over multiple retrievers and rerankers; C=1 dataset d

## Relevance for RAG-NIMBF
Candidate for the **Evaluation** axis at the weekly fit check.

## Status log
- 2026-11-04 screened
- 2026-11-09 fit check: rejected — timeline-constrained reranking — narrow evaluation niche, C=1 evidence
