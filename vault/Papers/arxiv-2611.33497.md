---
id: arxiv-2611.33497
title: "CA-RAG: Constraint-Aligned Retrieval for Structurally Faithful Long-Form Generation"
authors: [K. Vimal Kumar, Meghana Kshirsagar]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [Query-Transformation]
status: screened
screened: 2026-11-26
source: https://arxiv.org/abs/2611.33497
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.33497/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.33497/summary.md
tags: [rag-radar, query-transformation, knowledge-graph]
---
# CA-RAG: Constraint-Aligned Retrieval for Structurally Faithful Long-Form Generation

**Axis:** [[Query-Transformation]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.33497) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.33497/paper.pdf)

## Core idea
Condition retrieval queries with ontology-derived structural constraints and policy-grounded KG relations so evidence supports mandatory clauses in compliance-sensitive long-form generation.

## Results
> "At $k=6$, CA-RAG increases Precision@$k$ from $0.5268$ to $0.5692$, pooled Recall@$k$ from $0.5402$ to $0.5950$, and F1@$k$ from $0.5389$ to $0.5672$ over standard RAG." (Abstract / Sec. 5.1)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — constraint-aligned query expansion; three domains, manual annotation, ablations; CC BY 4.0, no public code found; feasible with domain ontology setup; query rewriting beyond HyDE/multi-hop not expressible.

## Relevance for RAG-NIMBF
New query-transformation value (constraint/KG expansion) needed → `new-axis.md` candidate.

## Status log
- 2026-11-26 screened
