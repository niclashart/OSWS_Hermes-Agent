---
id: arxiv-2610.30611
title: "Better Reasoning, Not Just Bigger Models: A Structure-Grounded Framework for Efficient and Reliable Inference"
authors: [SGUR authors]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 2, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-10-23
source: https://arxiv.org/abs/2610.30611
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.30611/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.30611/summary.md
tags: [rag-radar, New-Techniques]
---
# Better Reasoning, Not Just Bigger Models: A Structure-Grounded Framework for Efficient and Reliable Inference

**Axis:** [[New-Techniques]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2610.30611) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.30611/paper.pdf)

## Core idea
SGUR: training-free agentic framework aligning a query graph with candidate hypothesis graphs via prior-weighted partial matching and active information-gain node querying to prune the candidate space.

## Results
> "starting from only two observed symptoms, SGUR achieves 92.5% Hit@3, outperforming the strongest Graph-RAG baseline by 9.4 percentage points while using approximately 5x fewer tokens" (Abstract)

## Rubric
A: 2, B: 2, C: 1, D: 2, E: 0 — PrimeKG benchmark + ablations; training-free; code availability unclear (C=1)

## Relevance for RAG-NIMBF
Agentic active graph-querying loop - not expressible in RAG-NIMBF (new axis: agentic/active retrieval). Weekly-fit candidate.

## Status log
- 2026-10-23 screened
