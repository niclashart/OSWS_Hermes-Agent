---
id: arxiv-2611.02387
title: "EviCast: Forecasting Retrieval Gains Through Shared Response Calibration"
authors: [et al.]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 2, D: 1, E: 1}
axis: [Evaluation]
status: screened
screened: 2026-11-04
source: https://arxiv.org/abs/2611.02387
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.02387/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.02387/summary.md
tags: [rag-radar, Evaluation]
---
# EviCast: Forecasting Retrieval Gains Through Shared Response Calibration

**Axis:** [[Evaluation]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.02387) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.02387/paper.pdf)

## Core idea
Forecasts end-to-end net utility of RAG configurations before deployment by calibrating a generator's response to controlled evidence states once and combining with offline retriever evidence-state distributions — no full benchmark runs needed.

## Results
> "EviCast correctly decides all 14 HotpotQA retrieval configurations with a forecast error of 2.75 F1 points while reducing diagnostic generation calls by 80%."…

## Rubric
A 2 · B 2 · C 2 · D 1 · E 1 — pre-benchmark retrieval-value forecasting (Evaluation); B=2 14-24 configurations, theory + ablations; C=2 code; D=1 needs LLM generation calls; E=1 new pre-scre

## Relevance for RAG-NIMBF
Candidate for the **Evaluation** axis at the weekly fit check.

## Status log
- 2026-11-04 screened
