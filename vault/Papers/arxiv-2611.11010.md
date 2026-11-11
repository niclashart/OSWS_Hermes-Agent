---
id: arxiv-2611.11010
title: "Lightfoot: Graph Retrieval-Augmented Generation with Exact, Model-Free Document Deletion"
authors: [Uday Allu]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 2, D: 1, E: 1}
axis: [New-Techniques]
status: screened
screened: 2026-11-11
source: https://arxiv.org/abs/2611.11010
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.11010/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.11010/summary.md
tags: [rag-radar, New-Techniques]
---
# Lightfoot: Graph RAG with Exact, Model-Free Document Deletion

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.11010) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.11010/paper.pdf)

## Core idea
GraphRAG with chunk-level provenance: every edge is a deterministic function of per-passage extractions, so document deletion is a pure DB operation that reproduces a fresh index; retrieval is model-free (PPR + local cross-encoder).

## Results
> "Lightfoot builds the cheapest index on all three datasets, 26-31% below HippoRAG 2 and 3-6x below LightRAG and fast-graphrag." (Abstract)

## Rubric
A 2 · B 2 · C 2 · D 1 · E 1 — index cost + deletion invariant as new benchmarkable properties; graph RAG needs a new adapter + lifecycle metrics.

## Relevance for RAG-NIMBF
Graph RAG and lifecycle metrics not expressible today → New-Techniques.

## Status log
- 2026-11-11 screened
