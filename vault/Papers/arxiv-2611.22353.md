---
id: arxiv-2611.22353
title: "NONSENSE: Non-Semantic Strings Expose Semanticity Gaps in Dense Retrieval"
authors: [Ankit Gupta, et al.]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [Evaluation]
status: fit
screened: 2026-11-19
source: https://arxiv.org/abs/2611.22353
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.22353/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.22353/summary.md
tags: [rag-radar, Evaluation]
---
# NONSENSE: Non-Semantic Strings Expose Semanticity Gaps in Dense Retrieval

**Axis:** [Evaluation] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.22353) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.22353/paper.pdf)

## Core idea
NONSENSE: Non-Semantic Strings Expose Semanticity Gaps in Dense Retrieval — see papers/ summary.

## Results

> "Across five BEIR-style datasets and three popular single-vector retrievers, these strings frequently outscore the retriever's own best judged query-relevant passage (QRP), and often rank first in the full corpus." (Abstract)
> "<verbatim quote with numbers>" (Sec. <x>)

## Rubric

A 2 - B 2 - C 1 - D 2 - E 1 — new evaluation probe for dense retrievers; 5 BEIR datasets; C=1; black-box probe runs cheap (D=2); evaluation-side integration (E=1)
A 8 · B 8 · C 8 · D 8 · E 8 — <one-line justification>

## Relevance for RAG-NIMBF
Evaluation axis: could become a custom retrieval metric (semanticity-gap probe) via custom_retrieval_metrics_mode / custom_metrics; needs new metric implementation.

## Status log
- 2026-11-19 screened
- 2026-11-23 weekly fit: fit
