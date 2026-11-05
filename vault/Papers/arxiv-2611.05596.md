---
id: arxiv-2611.05596
title: "RAGCompass: Generalizable Retriever Routing via Reranking"
authors: [RAGCompass authors]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [Retrieval]
status: screened
screened: 2026-11-05
source: https://arxiv.org/abs/2611.05596
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.05596/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.05596/summary.md
tags: [rag-radar, Retrieval]
---
# RAGCompass (Retriever Routing)

**Axis:** [[Retrieval]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.05596) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.05596/paper.pdf)

## Core idea
Routes each query to the best retriever by reading the retrieved passage sets themselves (contrastively fine-tuned reranker against the produced answer + comparison head), so routing generalizes to unseen retrievers and corpora where query-only routers fail.

## Results
> "RAGCompass improves answer F1 by 28% relative to the best fixed retriever, and outperforms fusion baselines, three query-only routers, and a prompted 8B language model" (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — query-adaptive retriever routing; +28% rel. F1 + generalization tests; license unclear; reranker-scale model; needs a routing component, not a config value.

## Relevance for RAG-NIMBF
Not expressible today (no per-query retriever selection); candidate new key like `retrieval_router` comparing fixed retrievers per query.

## Status log
- 2026-11-05 screened
