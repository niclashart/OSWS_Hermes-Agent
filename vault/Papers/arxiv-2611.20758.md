---
id: arxiv-2611.20758
title: "UniGraph: A Unified Graph-based Index for Dynamic Hybrid Dense-Sparse Vector Retrieval"
authors: [Keyu Chen, et al.]
year: 2026
score: 7
rubric: {A: 1, B: 2, C: 1, D: 2, E: 1}
axis: [Vector-Store]
status: screened
screened: 2026-11-19
source: https://arxiv.org/abs/2611.20758
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.20758/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.20758/summary.md
tags: [rag-radar, Vector-Store]
---
# UniGraph: A Unified Graph-based Index for Dynamic Hybrid Dense-Sparse Vector Retrieval

**Axis:** [Vector-Store] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.20758) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.20758/paper.pdf)

## Core idea
UniGraph: A Unified Graph-based Index for Dynamic Hybrid Dense-Sparse Vector Retrieval — see papers/ summary.

## Results

> "In the mixed-weight setting, UniGraph delivers 27.6%~52.3% higher QPS than the fastest baseline on each dataset at Recall@100 >= 0.95." (Abstract)
> "<verbatim quote with numbers>" (Sec. <x>)

## Rubric

A 1 - B 2 - C 1 - D 2 - E 1 — hybrid graph index for vector store axis; strong QPS results; C=1; runs standard hardware (D=2); needs new backend (E=1)
A 7 · B 7 · C 7 · D 7 · E 7 — <one-line justification>

## Relevance for RAG-NIMBF
Vector-Store axis supports chroma/lancedb only; a hybrid-graph index would be a new vector_db_backend value.

## Status log
- 2026-11-19 screened
