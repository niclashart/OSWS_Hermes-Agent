---
id: arxiv-2611.02766
title: "EffComp: Efficient Prompt Compression via Hybrid Reinforcement & Supervised Learning"
authors: [et al.]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [New-Techniques]
status: fit
screened: 2026-11-04
source: https://arxiv.org/abs/2611.02766
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.02766/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.02766/summary.md
tags: [rag-radar, New-Techniques]
---
# EffComp: Efficient Prompt Compression via Hybrid Reinforcement & Supervised Learning

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.02766) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.02766/paper.pdf)

## Core idea
Extractive prompt compression for RAG QA: a BERT-style reranker and sentence selector, trained with hybrid RL + supervised learning, cut context to a compression ratio while preserving LLM accuracy with minimal latency; extractive, so no hallucination risk.

## Results
> "EffComp outperforms state-of-the-art prompt compression methods achieving the best trade-off between compression ratio and accuracy with minimal latency."…

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — context compression under a token budget — explicitly not expressible today; B=2 multiple QA datasets vs SOTA; C=1 no code mentioned; D=2 BERT-size models; E=1 

## Relevance for RAG-NIMBF
New technique — not expressible today; candidate for new-axis.md at weekly fit check.

## Status log
- 2026-11-04 screened
- 2026-11-09 fit check: not expressible — new-axis.md on proposal/2026-W46
