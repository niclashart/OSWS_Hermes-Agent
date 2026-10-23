---
id: arxiv-2610.30710
title: "Automated Enrichment Analysis with GraphRAG: Efficient Multi-Database ORA Extraction and Biological Interpretation"
authors: [Guangcan Li]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 2, D: 2, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-10-23
source: https://arxiv.org/abs/2610.30710
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.30710/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.30710/summary.md
tags: [rag-radar, New-Techniques]
---
# Automated Enrichment Analysis with GraphRAG: Efficient Multi-Database ORA Extraction and Biological Interpretation

**Axis:** [[New-Techniques]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2610.30710) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.30710/paper.pdf)

## Core idea
GBOR-RAG: graph RAG over a multi-database term-gene knowledge graph; prize-collecting subgraph retrieval conditions the LLM, plus a claim-level faithfulness metric for generated interpretations.

## Results
> "graph-based ORA preserves conventional ORA results with high consistency (mean Pearson r=0.997) while reducing query time by a median of 37x (up to 48x)" (Abstract)

## Rubric
A: 2, B: 2, C: 2, D: 2, E: 0 — open code (github.com/ggnb367/GBOR-RAG), multiple baselines and ablations, consumer-feasible

## Relevance for RAG-NIMBF
Graph RAG not expressible in RAG-NIMBF (no graph adapter). new-axis.md candidate; claim-level faithfulness also an Evaluation-axis extension.

## Status log
- 2026-10-23 screened
