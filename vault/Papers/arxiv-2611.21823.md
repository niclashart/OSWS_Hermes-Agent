---
id: arxiv-2611.21823
title: "TUSI: A Citation-Grounded Graph-Based Benchmark"
authors: [Marzieh Karimi, et al.]
year: 2026
score: 8
rubric: {A: 1, B: 2, C: 2, D: 2, E: 1}
axis: [Datasets]
status: screened
screened: 2026-11-19
source: https://arxiv.org/abs/2611.21823
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.21823/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.21823/summary.md
tags: [rag-radar, Datasets]
---
# TUSI: A Citation-Grounded Graph-Based Benchmark

**Axis:** [Datasets] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.21823) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.21823/paper.pdf)

## Core idea
TUSI: A Citation-Grounded Graph-Based Benchmark — see papers/ summary.

## Results

> "Experimental results demonstrate that incorporating graph-based relations improves retrieval recall by up to 8 percentage points compared to standard baselines." (Abstract)
> "<verbatim quote with numbers>" (Sec. <x>)

## Rubric

A 1 - B 2 - C 2 - D 2 - E 1 — new domain RAG dataset (Persian legal); recall eval + MC QA; open data; consumer-GPU feasible; dataset adapter needed (E=1)
A 8 · B 8 · C 8 · D 8 · E 8 — <one-line justification>

## Relevance for RAG-NIMBF
Datasets axis: hf-generic adapter may load TUSI-QA if fields map (dataset_question_field etc.); graph-retrieval baseline itself not expressible.

## Status log
- 2026-11-19 screened
