---
id: arxiv-2611.03196
title: "Dhārā Bench: An Evidence-Oriented Retrieval Benchmark for Indian Knowledge Systems"
authors: [et al.]
year: 2026
score: 8
rubric: {A: 1, B: 2, C: 2, D: 2, E: 1}
axis: [Datasets]
status: screened
screened: 2026-11-04
source: https://arxiv.org/abs/2611.03196
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.03196/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.03196/summary.md
tags: [rag-radar, Datasets]
---
# Dhārā Bench: An Evidence-Oriented Retrieval Benchmark for Indian Knowledge Systems

**Axis:** [[Datasets]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.03196) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.03196/paper.pdf)

## Core idea
Retrieval benchmark for Indian Knowledge Systems: 325 questions, 60k chunks, 7,578 relevance links, plus conjugate groups that score complete multi-passage evidence sets, with a fixed Pyserini BM25 baseline.

## Results
> "BM25 achieves MRR@20 of 0.315, Recall@10 of 0.182, and nDCG@10 of 0.205. On the group-annotated subset, complete-evidence scores are CE_Recall@20 = 0.294 and CE_MRR@20 = 0.141."…

## Rubric
A 1 · B 2 · C 2 · D 2 · E 1 — domain-specific dataset (Datasets axis); B=2 large annotated corpus + baseline; C=2 code CC BY 4.0; D=2 CPU; E=1 needs a jsonl/hf-generic adapter with group-lev

## Relevance for RAG-NIMBF
Candidate for the **Datasets** axis at the weekly fit check.

## Status log
- 2026-11-04 screened
