---
id: arxiv-2610.41396
title: "ProSearch: Benchmarking Multi-Constraint Protocol Retrieval in Experimental Science"
authors: [et al.]
year: 2026
score: 9
rubric: {A: 2, B: 2, C: 2, D: 1, E: 2}
axis: [Datasets]
status: proposed
screened: 2026-11-02
source: https://arxiv.org/abs/2610.41396
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.41396/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.41396/summary.md
tags: [rag-radar, Datasets]
---
# ProSearch: Benchmarking Multi-Constraint Protocol Retrieval in Experimental Science

**Axis:** [[Datasets]] · **Score:** 9/10 · [arXiv](https://arxiv.org/abs/2610.41396) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.41396/paper.pdf)

## Core idea
Benchmark for retrieval of experimental-science protocols under 3–5 interdependent explicit constraints (numerical and negation constraints included): 1,515 queries, six domains, 60 experimental fields with dependencies, evidence-based relevance validation.

## Results
> "The best-performing retriever achieves an average nDCG@10 of only 0.290, which improves to 0.474 with reranking." (Abstract)

## Rubric
A 2 · B 2 · C 2 · D 1 · E 2 — new dataset/benchmark for the Datasets axis, loadable via `hf-generic`; reranking gain makes it a good reranker testbed.

## Relevance for RAG-NIMBF
`dataset.name: hf-generic` with custom fields + `custom_retrieval_metrics_mode: gold_doc` (nDCG@10). Constraint-aware ranking itself is a new technique.

## Status log
- 2026-11-02 screened
- 2026-11-02 fit-check (W45): expressible (Datasets axis) → proposals/arxiv-2610.41396/config.yaml (reranker arm, nDCG@10 gold_doc); status proposed
- 2026-11-11 impl-check: see implementations/2026-W46/arxiv-2610.41396.md
