---
id: arxiv-2611.29966
title: "Structure-Exploiting Hierarchical Retrieval for Long Narrative Documents: A Precision-Oriented Alternative to Learned Abstraction Trees"
authors: [Rohit Singh, Nathaniel Weems]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [New-Techniques]
status: screened
screened: 2026-11-24
source: https://arxiv.org/abs/2611.29966
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.29966/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.29966/summary.md
tags: [rag-radar, New-Techniques]
---
# Structure-Exploiting Hierarchical Retrieval for Long Narrative Documents

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.29966) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.29966/paper.pdf)

## Core idea
Native-structure two-level retriever: chapter selection via hybrid BM25+dense over recaps, chapter-filtered dense search, section-aware span expansion under token budget; content-hash delta ingestion reuses 94–99.7% of embeddings.

## Results
> "On QuALITY, hierarchical retrieval significantly beats flat top-$k$ (81.0% vs 70.4%, $p{=}0.0019$) and is statistically indistinguishable from feeding the full article ($p{=}0.74$)" (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — hybrid BM25+dense fusion and two-stage structural retrieval not in internal adapter.

## Relevance for RAG-NIMBF
Not expressible today: hybrid fusion explicitly listed under "Not expressible"; needs new retrieval component.

## Status log
- 2026-11-24 screened
