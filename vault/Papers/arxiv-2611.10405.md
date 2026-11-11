---
id: arxiv-2611.10405
title: "Yuanbao-Reranker: Document-Grounded Synthesis and Preference Distillation for Text Reranking"
authors: [Hongyuan Xu, Dezhi Ye, ...]
year: 2026
score: 9
rubric: {A: 2, B: 2, C: 1, D: 2, E: 2}
axis: [Reranking]
status: screened
screened: 2026-11-11
source: https://arxiv.org/abs/2611.10405
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.10405/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.10405/summary.md
tags: [rag-radar, Reranking]
---
# Yuanbao-Reranker

**Axis:** [[Reranking]] · **Score:** 9/10 · [arXiv](https://arxiv.org/abs/2611.10405) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.10405/paper.pdf)

## Core idea
Qwen3-based dense pointwise reranker family (0.6B/4B/8B) trained on 2.75M curated 1:3 ranking groups with false-negative filtering and hinge-distillation.

## Results
> "the 0.6B variant reaches 70.96 Avg. to surpass 1B–4B active-parameter baselines, the 4B variant reaches 73.63 Avg. to outperform the 8B teacher (72.68), and the 8B variant achieves a state-of-the-art 74.21 Avg." (Abstract; CMTEB-R/MMTEB-R/BEIR/MLDR/MTEB-Code)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 2 — beats bge-reranker class at every size; weight license to confirm on HF card; 0.6B consumer-GPU friendly; CrossEncoder slot value.

## Relevance for RAG-NIMBF
Candidate `reranker_models: huggingface:tencent/Yuanbao-Reranker-0.6B` (verify sentence-transformers CrossEncoder compatibility before proposing).

## Status log
- 2026-11-11 screened
