---
id: arxiv-2611.00450
title: "From Lookups to Lessons: Turning Retrieved Knowledge into Parametric Memory"
authors: [et al.]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 2, D: 2, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-11-04
source: https://arxiv.org/abs/2611.00450
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.00450/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.00450/summary.md
tags: [rag-radar, New-Techniques]
---
# From Lookups to Lessons: Turning Retrieved Knowledge into Parametric Memory

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.00450) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.00450/paper.pdf)

## Core idea
ResMem: distills retrieved evidence offline into a parametric memory that predicts an additive logit residual; cuts teacher-construction storage 94.7% vs kNN and breaks 21% fewer correct answers than a kNN-trained memory.

## Results
> "ResMem reduces the storage retained for teacher construction by 94.7% compared with the evaluated kNN pipeline. Across five question answering datasets, ResMem raises mean token F1 from 32.83% for the frozen LLM to 34.48%."…

## Rubric
A 2 · B 2 · C 2 · D 2 · E 0 — retrieval-to-parametric-memory; B=2 five QA datasets; C=2 code + HF weights (MIT/Apache family); D=2 7B Mistral quantized; E=0: requires a training loop — not e

## Relevance for RAG-NIMBF
New technique — not expressible today; candidate for new-axis.md at weekly fit check.

## Status log
- 2026-11-04 screened
