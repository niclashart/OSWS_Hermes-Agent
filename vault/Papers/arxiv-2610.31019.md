---
id: arxiv-2610.31019
title: "Chunk Recomputation under Real Document Revisions: Measuring Update Cost and Retrieval Quality of Fixed, Recursive, and Content-Defined Chunking"
authors: [Yuning Bian]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [Chunking]
status: screened
screened: 2026-10-23
source: https://arxiv.org/abs/2610.31019
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.31019/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.31019/summary.md
tags: [rag-radar, Chunking]
---
# Chunk Recomputation under Real Document Revisions: Measuring Update Cost and Retrieval Quality of Fixed, Recursive, and Content-Defined Chunking

**Axis:** [[Chunking]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2610.31019) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.31019/paper.pdf)

## Core idea
Measures embedding update cost of chunkers under real document revisions: fixed-size chunking recomputes 57-68% of embedding workload per revision, recursive 38-56%, content-defined 43-54%, while evidence recall differs by less than 2pp.

## Results
> "fixed-size chunking recomputes 57-68% of its full new-version embedding-input workload, recursive chunking 38-56%, and content-defined chunking 43-54% ... while at these parameters mean evidence recall under a fixed 2048-token retrieval budget differs by less than two percentage points within either language" (Abstract)

## Rubric
A: 2, B: 2, C: 1, D: 2, E: 1 — 120 bilingual revision pairs, controlled edits, ablations; Steadlith implementation Apache-2.0; frozen dense encoder on consumer GPU

## Relevance for RAG-NIMBF
Update cost is a new evaluation dimension for the Chunking axis; content-defined chunking (Steadlith) pluggable as a new chunking strategy value. Strong weekly-fit candidate.

## Status log
- 2026-10-23 screened
