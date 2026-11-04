---
id: arxiv-2611.01409
title: "RAG-TRACE: Tracing Measurement Evidence and Diagnostic Completeness in AI-Generated ECG Reports"
authors: [et al.]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 1, E: 1}
axis: [Evaluation]
status: screened
screened: 2026-11-04
source: https://arxiv.org/abs/2611.01409
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.01409/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.01409/summary.md
tags: [rag-radar, Evaluation]
---
# RAG-TRACE: Tracing Measurement Evidence and Diagnostic Completeness in AI-Generated ECG Reports

**Axis:** [[Evaluation]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.01409) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.01409/paper.pdf)

## Core idea
Shows retrieved diagnostic criteria in RAG-generated ECG reports often lack patient-specific measurement support; retrieval increased unsupported-criterion reports; deterministic measurement verification removes most unsupported applications.

## Results
> "Under matched instructions and an identical output schema, retrieval increased unsupported-criterion reports from 17.4% to 31.1%, while hypertrophy recall remained unchanged at 62.6%."…

## Rubric
A 2 · B 2 · C 1 · D 1 · E 1 — evidence-support verification as an evaluation dimension — retrieval can hurt factuality (Evaluation); B=2 1,083 records + controlled experiments; C=1 no code m

## Relevance for RAG-NIMBF
Candidate for the **Evaluation** axis at the weekly fit check.

## Status log
- 2026-11-04 screened
