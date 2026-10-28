---
id: arxiv-2610.37231
title: "TaskBridge: Technical Report for SIGIR 2026 eCommerce Challenge"
authors: [(abstract only; authors not fetched)]
year: 2026
score: 7
rubric: {A: 2, B: 1, C: 1, D: 2, E: 1}
axis: [Query-Transformation]
status: screened
screened: 2026-10-28
source: https://arxiv.org/abs/2610.37231
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.37231/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.37231/summary.md
tags: [rag-radar, Query-Transformation]
---
# TaskBridge: Technical Report for SIGIR 2026 eCommerce Challenge

**Axis:** [[Query-Transformation]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2610.37231) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.37231/paper.pdf)

## Core idea
Reformulates task-oriented queries into product-retrieval expressions by grounding them in catalog vocabulary: Catalog Semantic Anchoring, Unified Five-Candidate Rewriting, and Protocol-Aware Selection, followed by BM25 retrieval.

## Results
> "These queries often imply product needs through activity-level semantics, creating a lexical gap with catalog descriptions." (Abstract, motivation)

## Rubric
A 2 · B 1 · C 1 · D 2 · E 1 — Query rewriting clearly beyond HyDE; single challenge task; code unclear; LLM rewriting cheap on consumer hardware; multi-candidate rewriting/selection needs a new component.

## Relevance for RAG-NIMBF
Candidate value for `matrix.retrieval_use_hyde` or a new adapter component; decide in weekly fit check.

## Status log
- 2026-10-28 screened
