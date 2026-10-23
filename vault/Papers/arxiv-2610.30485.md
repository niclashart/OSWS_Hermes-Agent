---
id: arxiv-2610.30485
title: "Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences"
authors: [MemPABench authors]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 2, D: 2, E: 0}
axis: [Datasets]
status: screened
screened: 2026-10-23
source: https://arxiv.org/abs/2610.30485
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.30485/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.30485/summary.md
tags: [rag-radar, Datasets]
---
# Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences

**Axis:** [[Datasets]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2610.30485) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.30485/paper.pdf)

## Core idea
Interactive benchmark (MemPABench) for on-policy evaluation of agent memory over interaction preferences: 99 sessions, preference changes over four months, evaluating Mem0/MemOS/simple RAG/file-based memory.

## Results
> "Retrieval-based systems (i.e. Mem0, MemOS, simple RAG) do not outperform No Memory, while File-based memory improves accuracy but applies preferences beyond relevant contexts" (Abstract)

## Rubric
A: 2, B: 2, C: 2, D: 2, E: 0 — environment and dataset public (mempabench.com), four memory systems x four LLM backbones, consumer-feasible

## Relevance for RAG-NIMBF
Evaluation dataset covering simple RAG as baseline; needs a new environment adapter - candidate for Datasets/Evaluation extension. Weekly-fit candidate.

## Status log
- 2026-10-23 screened
