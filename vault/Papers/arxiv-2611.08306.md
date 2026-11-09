---
id: arxiv-2611.08306
title: "GINGER: Spicing Up Graph-Based Vector Search"
authors: [Daniel Salwasser, Lars Gottesbüren, Laxman Dhulipala, Guy Blelloch, Rajesh Jayaram, Amir Zandieh, Vahab Mirrokni]
year: 2026
score: 7
rubric: {A: 1, B: 2, C: 2, D: 2, E: 0}
axis: [Vector-Store]
status: rejected
screened: 2026-11-07
source: https://arxiv.org/abs/2611.08306
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.08306/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.08306/summary.md
tags: [rag-radar, vector-store]
---
# GINGER: Spicing Up Graph-Based Vector Search

**Axis:** [[Vector-Store]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.08306) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.08306/paper.pdf)

## Core idea
Open-source C++ ANNS library (Google): Nested TurboQuant (4-bit navigation + precise reranking in one representation), graph reordering + AdaptiveGap lossless codec, PCA projection and beam-search optimizations.

## Results
> "At 95% recall, Ginger speeds up query throughput by an average of 1.8× over each dataset's fastest competitor and by at least 2.3× over any single library." (Abstract)

## Rubric
A 1 · B 2 · C 2 · D 2 · E 0 — index-internal codec; RAG-NIMBF only selects `vector_db_backend` (chroma/lancedb), no ANNS-library slot.

## Relevance for RAG-NIMBF
Not expressible as a config value — informational efficiency reference for the Vector-Store axis.

## Status log
- 2026-11-07 screened
- 2026-11-09 fit check: rejected — ANN library internals, E=0 — covered by vector_db_backend swap, no pluggable-index slot planned
