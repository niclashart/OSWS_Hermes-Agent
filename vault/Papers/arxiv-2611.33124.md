---
id: arxiv-2611.33124
title: "SAG-Mem-1.0 Technical Report"
authors: [n/a]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 2, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-11-25
source: https://arxiv.org/abs/2611.33124
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.33124/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.33124/summary.md
tags: [rag-radar, New-Techniques]
---
# SAG-Mem-1.0 Technical Report

**Axis:** [[New-Techniques]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.33124) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.33124/paper.pdf)

## Core idea
Conversational long-term memory keeping full dialogue chunks with a BM25 lexical index (no LLM memory construction); evidence evaluation and lexical cues guide a second query-time retrieval round.

## Results
> "On LongMemEval, it exceeds the strongest compared baseline by 7.20 points." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 0 — lexical-expansion memory loop; two benchmarks, strong baselines; no code; consumer-GPU feasible; not expressible (no BM25/hybrid, no evidence-evaluator loop).

## Relevance for RAG-NIMBF
Needs hybrid BM25 retrieval + evidence-guided retrieval expansion as new axis values.

## Status log
- 2026-11-25 screened
