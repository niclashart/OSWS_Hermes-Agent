---
id: arxiv-2611.32917
title: "SOARS: System One Assisted Reranking for Agentic Search"
authors: [n/a]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 1, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-11-25
source: https://arxiv.org/abs/2611.32917
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.32917/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.32917/summary.md
tags: [rag-radar, New-Techniques]
---
# SOARS: System One Assisted Reranking for Agentic Search

**Axis:** [[New-Techniques]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.32917) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.32917/paper.pdf)

## Core idea
Training-free LLM ("System One") reranking at each step of an agentic deep search — single-call calibrated relevance over question + sub-query, reducing search calls and cost.

## Results
> "improves GPT-5.4 Mini's accuracy from 73.9% to 84.7% while reducing search calls from 23 to 14" (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 1 · E 0 — LLM reranking in agentic loop; six backbones, two benchmarks; CC BY-NC-ND, no code; big LLM backbones; new provider needed.

## Relevance for RAG-NIMBF
LLM reranking provider + per-round reranking in iterative retrieval — not expressible today.

## Status log
- 2026-11-25 screened
