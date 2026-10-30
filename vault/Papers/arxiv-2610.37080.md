---
id: arxiv-2610.37080
title: "Tessera: Structure-Completed Evidence Units for Web Retrieval-Augmented Generation"
authors: [(abstract only; authors not fetched)]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [Chunking]
status: screened
screened: 2026-10-28
source: https://arxiv.org/abs/2610.37080
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.37080/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.37080/summary.md
tags: [rag-radar, Chunking]
---
# Tessera: Structure-Completed Evidence Units for Web Retrieval-Augmented Generation

**Axis:** [[Chunking]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2610.37080) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.37080/paper.pdf)

## Core idea
Decouples retrieval from reading: rebuilds retrieved pages' HTML into fine-grained evidence units completed with page title, section path, and table headers, then packs query-relevant units into the reader context. Applies to text, screenshot, and agentic pipelines.

## Results
> "Across three question answering benchmarks, Tessera improves answer accuracy by 5 to 6 points on text and screenshot pipelines, consistently across readers, retrievers, and reader budgets" (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — New evidence-unit option for the Chunking axis; full English Wikipedia, three benchmarks, matched-budget baselines; code unclear; training-free; needs a new post-retrieval delivery component.

## Relevance for RAG-NIMBF
Candidate value for `matrix.chunking_strategies` or a new adapter component; decide in weekly fit check.

## Status log
- 2026-10-28 screened
- 2026-10-30 impl-check: NIMBF missing, Blueprint partial
