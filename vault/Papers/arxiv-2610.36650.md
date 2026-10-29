---
id: arxiv-2610.36650
title: "TACO-Graph: Automated Construction of Text-Atributed Graphs"
authors: [Amiri Hayes, Kristina Wicke]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 2, D: 2, E: 1}
axis: [New-Techniques]
status: screened
screened: 2026-10-29
source: https://arxiv.org/abs/2610.36650
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.36650/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.36650/summary.md
tags: [rag-radar, New-Techniques]
---
# TACO-Graph: Automated Construction of Text-Atributed Graphs

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2610.36650) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.36650/paper.pdf)

## Core idea
Decision trees learn which text-attributed-graph construction choices (node entity, edge semantics, node text) perform best per dataset and task, using cheap proxy evaluations (GNN accuracy, RAGAS for GraphRAG retrieval) on small subsets. Open-source pipeline.

## Results
> "our decision trees predict construction quality on separately drawn evaluation samples with mean Spearman ρ above 0.9 for node classification and above 0.8 for GraphRAG retrieval" (Abstract)

## Rubric
A 2 · B 2 · C 2 · D 2 · E 1 — graph-RAG construction search, 5 datasets, open code CC BY 4.0, consumer-GPU proxy scoring; needs new graph component in RAG-NIMBF.

## Relevance for RAG-NIMBF
Not expressible: graph RAG is a known gap → [[New-Techniques]]. Would need a graph-construction axis (node entity policy, edge semantics, node text).

## Status log
- 2026-10-29 screened
