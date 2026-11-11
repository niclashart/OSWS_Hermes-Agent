---
id: arxiv-2611.10238
title: "CoRA-Bench: Evaluating Evidence Preservation by Context Selectors Under Token Budgets"
authors: [anonymous]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 2, D: 1, E: 1}
axis: [Evaluation, Datasets]
status: screened
screened: 2026-11-11
source: https://arxiv.org/abs/2611.10238
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.10238/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.10238/summary.md
tags: [rag-radar, Evaluation]
---
# CoRA-Bench

**Axis:** [[Evaluation]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.10238) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.10238/paper.pdf)

## Core idea
Benchmark for context-selection methods under shared token budgets, measuring evidence preservation and downstream accuracy across four long-context datasets.

## Results
> "BM25 achieves 0.921 supporting-fact recall on BABILong at 128K, dense retrieval and dense reranking each achieve 0.908 needle recall on NoLiMa at 64K" (Abstract)

## Rubric
A 2 · B 2 · C 2 · D 1 · E 1 — benchmarks the missing context-compression axis; public benchmark; budget protocol needs a new component.

## Relevance for RAG-NIMBF
Candidate `hf-generic` dataset; token-budget selection protocol itself → New-Techniques.

## Status log
- 2026-11-11 screened
