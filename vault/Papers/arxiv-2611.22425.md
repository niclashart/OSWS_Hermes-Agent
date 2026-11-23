---
id: arxiv-2611.22425
title: "LMMR: Learned Multigranular Memory Retrieval for Small Language Model Agents"
authors: [Pengfeng Song, et al.]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 1, E: 1}
axis: [Retrieval]
status: fit
screened: 2026-11-19
source: https://arxiv.org/abs/2611.22425
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.22425/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.22425/summary.md
tags: [rag-radar, Retrieval]
---
# LMMR: Learned Multigranular Memory Retrieval for Small Language Model Agents

**Axis:** [Retrieval] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.22425) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.22425/paper.pdf)

## Core idea
LMMR: Learned Multigranular Memory Retrieval for Small Language Model Agents — see papers/ summary.

## Results

> "On 22,398 official validation questions from HotpotQA, 2WikiMultihopQA, and MuSiQue, a frozen 2B answer model reaches 61.47, 43.26, and 30.58 F1 under a 400-token budget." (Abstract)
> "<verbatim quote with numbers>" (Sec. <x>)

## Rubric

A 2 - B 2 - C 1 - D 1 - E 1 — learned budgeted evidence selection = new technique; 3 datasets + significance; training required (C=1, E=1); 2B models feasible (D=1)
A 7 · B 7 · C 7 · D 7 · E 7 — <one-line justification>

## Relevance for RAG-NIMBF
Not expressible: learned selection beyond similarity/MMR/multi-hop. Weekly fit check -> new-axis.md.

## Status log
- 2026-11-19 screened
- 2026-11-23 weekly fit: fit
