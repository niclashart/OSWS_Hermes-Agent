---
id: arxiv-2611.09807
title: "Compaction, decay and reinforcement in a two-tier conversational memory: a paired evaluation against retrieval-augmented generation"
authors: [Osamudiamen Edogun, Joshua Obigwe]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 2, D: 1, E: 1}
axis: [New-Techniques]
status: fit
screened: 2026-11-09
source: https://arxiv.org/abs/2611.09807
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.09807/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.09807/summary.md
tags: [rag-radar, New-Techniques, memory]
---
# Compaction, decay and reinforcement in a two-tier conversational memory

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.09807) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.09807/paper.pdf)

## Core idea
Compacting conversation turns into atomic facts in a two-tier store beats transcript RAG by 6.8 points (p=5.5e-08) at 34% fewer prompt tokens on LoCoMo, but loses on adversarial questions where the answer is a phrasing, not a value.

## Results
> "compaction scores 71.4 per cent against 64.6, a lead of 6.8 points (p = 5.5e-08) at 34 per cent fewer prompt tokens" (Abstract)

## Rubric
A 2 · B 2 · C 2 · D 1 · E 1 — paired McNemar evaluation, full code release; ingestion needs paid API; memory compaction not a RAG-NIMBF axis.

## Relevance for RAG-NIMBF
Not expressible: needs a memory/compaction component (new axis candidate).

## Status log
- 2026-11-09 screened
- 2026-11-09 fit check: not expressible — new-axis.md on proposal/2026-W46
