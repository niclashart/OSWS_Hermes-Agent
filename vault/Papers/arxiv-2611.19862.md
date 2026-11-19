---
id: arxiv-2611.19862
title: "Bioformer-RetroMAE: retrieval-oriented pretraining of a compact biomedical language model for literature search"
authors: [Jialu Li, et al.]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [Embedding]
status: screened
screened: 2026-11-19
source: https://arxiv.org/abs/2611.19862
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.19862/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.19862/summary.md
tags: [rag-radar, Embedding]
---
# Bioformer-RetroMAE: retrieval-oriented pretraining of a compact biomedical language model for literature search

**Axis:** [Embedding] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.19862) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.19862/paper.pdf)

## Core idea
Bioformer-RetroMAE: retrieval-oriented pretraining of a compact biomedical language model for literature search — see papers/ summary.

## Results

> "Compared with PubMedBERT, it improved mean average precision (MAP) by 37.0% and Recall@100 by 29.1%." (Abstract)
> "<verbatim quote with numbers>" (Sec. <x>)

## Rubric

A 2 - B 2 - C 1 - D 2 - E 1 — compact domain embedder for Embedding axis; big MAP gains vs domain baselines; C=1; 43M params trivially feasible (D=2); HF embedder value (E=1)
A 8 · B 8 · C 8 · D 8 · E 8 — <one-line justification>

## Relevance for RAG-NIMBF
Embedding axis: huggingface:<id> if weights are sentence-transformers loadable; verify license at fit check.

## Status log
- 2026-11-19 screened
