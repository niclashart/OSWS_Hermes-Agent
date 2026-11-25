---
id: arxiv-2611.30588
title: "SuSi-RAG: A Hybrid Graph RAG for Equipment Maintenance"
authors: [Hansi Zhang, Wilma Johanna Schmidt]
year: 2026
score: 7
rubric: {A: 2, B: 1, C: 1, D: 1, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-11-25
source: https://arxiv.org/abs/2611.30588
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.30588/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.30588/summary.md
tags: [rag-radar, New-Techniques]
---
# SuSi-RAG: A Hybrid Graph RAG for Equipment Maintenance

**Axis:** [[New-Techniques]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.30588) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.30588/paper.pdf)

## Core idea
Hybrid Graph RAG matching query and maintenance record via subgraph similarity; in production on a Bosch line for 8+ months with an operational feedback loop.

## Results
> "SuSi-RAG improves top-1 retrieval accuracy from 61.5% to 96.2% and expert-rated answer quality from 44.9% to 84.1% against a vector-based baseline" (Abstract)

## Rubric
A 2 · B 1 · C 1 · D 1 · E 0 — subgraph-similarity graph retrieval; PoC with baseline, domain-specific, no public code; industrial deployment; not expressible.

## Relevance for RAG-NIMBF
Confirms gap: graph/knowledge-graph retrieval axis missing.

## Status log
- 2026-11-25 screened
