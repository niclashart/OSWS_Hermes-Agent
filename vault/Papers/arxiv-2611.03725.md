---
id: arxiv-2611.03725
title: "From Logs to Faults: Reference-Free Fault Localization for Retrieval-Augmented Generation Pipelines"
authors: [Hira Naveed, Scott Barnett, Stefanus Kurniawan, John Grundy, Chetan Arora, Hourieh Khalajzadeh, Omar Haggag]
year: 2026
score: 9
rubric: {A: 2, B: 2, C: 2, D: 2, E: 1}
axis: [Evaluation]
status: fit
screened: 2026-11-07
source: https://arxiv.org/abs/2611.03725
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.03725/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.03725/summary.md
tags: [rag-radar, evaluation]
---
# From Logs to Faults: Reference-Free Fault Localization for RAG Pipelines (RAGLog)

**Axis:** [[Evaluation]] · **Score:** 9/10 · [arXiv](https://arxiv.org/abs/2611.03725) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.03725/paper.pdf)

## Core idea
RAGLog localizes faults per RAG stage (rewriter/embedder/retriever/reranker/generator) from execution logs — no reference answers or instrumentation. Rule-based + embedding-based + LLM-based stage checks feed an ensemble fault classifier; open-source tool plus a 3,134-run labeled fault dataset.

## Results
> "RAGLog achieves a pooled F1 score of 0.73 on runs with naturally occurring faults, outperforming Claude Code (0.58) and Codex (0.52)" (Abstract); ~5 s and US$0.005 per run. "Among the 551 naturally faulty runs … 202 (37%) still produced correct answers" (Sec. 8.1) — answer-level evaluation misses these faults.

## Rubric
A 2 · B 2 · C 2 · D 2 · E 1 — stage-level fault localization is a new evaluation capability; needs an adapter over per-stage logs.

## Relevance for RAG-NIMBF
Not expressible as pure config: needs a fault-localization evaluation component that consumes per-stage run logs. Candidate for `new-axis.md`.

## Status log
- 2026-11-07 screened
- 2026-11-09 fit check: not expressible — new-axis.md on proposal/2026-W46
