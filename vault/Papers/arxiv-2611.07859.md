---
id: arxiv-2611.07859
title: "CORE: Coarse-to-Fine Search with Context Management for Deep Research"
authors: [Hoang Tran Vuong, Ngoc Quan Pham, Hung Bui, Fatih Porikli, Dat Quoc Nguyen]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [New-Techniques]
status: screened
screened: 2026-11-07
source: https://arxiv.org/abs/2611.07859
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.07859/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.07859/summary.md
tags: [rag-radar, new-techniques]
---
# CORE: Coarse-to-Fine Search with Context Management for Deep Research

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.07859) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.07859/paper.pdf)

## Core idea
Training-free deep-research harness: dense retrieval, then ColBERT reranker's token-similarity matrix is reused to return only the best snippet per passage; context expansion around previously retrieved sources and cross-search snippet deduplication keep the agent context small.

## Results
> "CORE achieves state-of-the-art answer accuracy and evidence recall across three agent models and three benchmarks (BrowseComp-Plus, BrowseComp-Wikipedia and BrowseComp-Plus-CM), on corpora containing up to 553M documents." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — context compression/selection under token budget + agentic search, both on the not-expressible list.

## Relevance for RAG-NIMBF
Needs new axes/components: snippet selection, context expansion, cross-search dedup. Not expressible today.

## Status log
- 2026-11-07 screened
