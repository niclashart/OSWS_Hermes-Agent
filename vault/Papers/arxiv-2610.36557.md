---
id: arxiv-2610.36557
title: "QESChunker: A Single Objective Unifies Overlapping and Non-Overlapping Chunking for RAG"
authors: [(abstract only; authors not fetched)]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [Chunking]
status: screened
screened: 2026-10-28
source: https://arxiv.org/abs/2610.36557
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.36557/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.36557/summary.md
tags: [rag-radar, Chunking]
---
# QESChunker: A Single Objective Unifies Overlapping and Non-Overlapping Chunking for RAG

**Axis:** [[Chunking]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2610.36557) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.36557/paper.pdf)

## Core idea
First supervised chunker: builds document-specific static chunk indices by maximizing question-evidence utility from human- or LLM-generated pairs. Non-overlap is solvable exactly by dynamic programming; the overlapping case is monotone submodular, optimized with a (1-1/sqrt(e))-approximation greedy.

## Results
> "Across two self-constructed and three public datasets, both variants outperform existing chunking methods in complete-evidence recall in nearly all evaluated settings, under the same overlap regime and a fixed hybrid retriever." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — Clear new chunking option; five datasets, same-overlap comparison; code/license unclear; static index construction, no retriever training; not a pluggable chunker value today — new chunker component needed.

## Relevance for RAG-NIMBF
Candidate value for `matrix.chunking_strategies` or a new adapter component; decide in weekly fit check.

## Status log
- 2026-10-28 screened
