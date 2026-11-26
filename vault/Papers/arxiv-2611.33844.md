---
id: arxiv-2611.33844
title: "When Rerankers Work Together: Better and Faster Reranking without Joint Training"
authors: [Yanqiao Chen, Dongsheng Hou, Yuhan Rui]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [Reranking]
status: screened
screened: 2026-11-26
source: https://arxiv.org/abs/2611.33844
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.33844/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.33844/summary.md
tags: [rag-radar, reranking]
---
# When Rerankers Work Together: Better and Faster Reranking without Joint Training

**Axis:** [[Reranking]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.33844) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.33844/paper.pdf)

## Core idea
Heterogeneous reranker cascades without joint training: trained cacheable coarse scorers (Cache-Pointwise, Cache-Shapley) prune candidates before CrossEncoder/Provence/ColBERTv2, improving accuracy and speed at matched budgets.

## Results
> "On NoLiMa 32K with Gemma, inserting these scorers before CrossEncoder or Provence improves answer accuracy by 4.02-9.43 percentage points while accelerating online pruning by 1.57-1.88x relative to the corresponding reranker alone." (Abstract)
> "a cascade can outperform its final reranker alone while underperforming its coarse selector alone" (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — new multistage reranking technique; two datasets + ablations; CC BY 4.0, no public code found; consumer-GPU feasible; cascade not expressible (single reranker slot only).

## Relevance for RAG-NIMBF
Needs multi-stage reranking / per-stage candidate budgets / RRF fusion → `new-axis.md` candidate.

## Status log
- 2026-11-26 screened
