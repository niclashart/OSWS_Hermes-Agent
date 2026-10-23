---
id: arxiv-2610.31256
title: "IndoNutriQA: An Indonesian Clinical Nutrition Question Answering Benchmark"
authors: [Tirana Noor Fatyanosa]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 2, D: 2, E: 0}
axis: [Datasets]
status: screened
screened: 2026-10-23
source: https://arxiv.org/abs/2610.31256
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.31256/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.31256/summary.md
tags: [rag-radar, Datasets]
---
# IndoNutriQA: An Indonesian Clinical Nutrition Question Answering Benchmark

**Axis:** [[Datasets]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2610.31256) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.31256/paper.pdf)

## Core idea
Expert-curated Indonesian clinical-nutrition QA benchmark: 911 QA pairs from 120 real reports, chunk-segmentation metadata, RAG baselines, LLM-as-judge calibrated against three expert raters.

## Results
> "every pair is grounded in a clinically relevant context, enriched with structured metadata (anthropometric assessment, medical diagnosis, document provenance, chunk segmentation)" (Abstract)

## Rubric
A: 2, B: 2, C: 2, D: 2, E: 0 — open data and code (github.com/NLP-UB/IndoNutriQA), multi-baseline experiments incl. RAG, consumer-feasible

## Relevance for RAG-NIMBF
New dataset with chunk metadata; needs a registered dataset adapter in RAG-NIMBF. Weekly-fit candidate (new dataset value).

## Status log
- 2026-10-23 screened
