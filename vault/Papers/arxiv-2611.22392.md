---
id: arxiv-2611.22392
title: "Deal With It: On Better Schedules for Listwise Reranking"
authors: [Benjamin Clavié, et al.]
year: 2026
score: 9
rubric: {A: 2, B: 2, C: 2, D: 2, E: 1}
axis: [Reranking]
status: screened
screened: 2026-11-19
source: https://arxiv.org/abs/2611.22392
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.22392/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.22392/summary.md
tags: [rag-radar, Reranking]
---
# Deal With It: On Better Schedules for Listwise Reranking

**Axis:** [Reranking] · **Score:** 9/10 · [arXiv](https://arxiv.org/abs/2611.22392) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.22392/paper.pdf)

## Core idea
Deal With It: On Better Schedules for Listwise Reranking — see papers/ summary.

## Results

> "In existing schedules such as BlitzRank, dealing reduces repair calls from 59% of queries to 14%, improving latency with no significant change in quality." (Abstract)
> "<verbatim quote with numbers>" (Sec. <x>)

## Rubric

A 2 - B 2 - C 2 - D 2 - E 1 — LLM listwise reranking schedule = new provider in Reranking axis; strong theory + 6-LLM experiments; open code (C=2); API-based (D=2); schedule plug-in (E=1)
A 9 · B 9 · C 9 · D 9 · E 9 — <one-line justification>

## Relevance for RAG-NIMBF
Reranking axis only supports cross-encoder reranker_models; LLM listwise schedules = new provider. Weekly fit check -> new-axis.md.

## Status log
- 2026-11-19 screened
