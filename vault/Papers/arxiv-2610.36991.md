---
id: arxiv-2610.36991
title: "SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation"
authors: [(abstract only; authors not fetched)]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 1, E: 1}
axis: [New-Techniques]
status: screened
screened: 2026-10-28
source: https://arxiv.org/abs/2610.36991
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.36991/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.36991/summary.md
tags: [rag-radar, New-Techniques]
---
# SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2610.36991) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.36991/paper.pdf)

## Core idea
Builds a weighted chunk graph (semantic similarity, document adjacency, section hierarchy, shared entities, citation links, LLM-generated utility questions), expands a hybrid seed set over the graph, re-scores via spectral relevance propagation, and assembles context under a fixed token budget.

## Results
> "Experiments on MultiHopRAG, UltraDomain, and long-document question-answering settings show that SpectRAG improves broad evi[dence coverage]" (Abstract; truncated at fetch)

## Rubric
A 2 · B 2 · C 1 · D 1 · E 1 — Graph RAG technique; three settings including MultiHopRAG; code unclear; per-chunk LLM utility questions add cost but feasible; graph retrieval not expressible in NIMBF.

## Relevance for RAG-NIMBF
Not expressible today — graph/conflict-handling technique; weekly fit check should produce `new-axis.md`.

## Status log
- 2026-10-28 screened
- 2026-10-30 impl-check: NIMBF missing, Blueprint not-applicable
