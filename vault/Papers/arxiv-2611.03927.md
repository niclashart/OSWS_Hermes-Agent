---
id: arxiv-2611.03927
title: "Modular and Efficient Approximate Nearest Neighbors Search with Vectorium and kANNolo"
authors: [et al.]
year: 2026
score: 8
rubric: {A: 1, B: 2, C: 2, D: 2, E: 1}
axis: [Vector-Store]
status: screened
screened: 2026-11-04
source: https://arxiv.org/abs/2611.03927
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.03927/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.03927/summary.md
tags: [rag-radar, Vector-Store]
---
# Modular and Efficient Approximate Nearest Neighbors Search with Vectorium and kANNolo

**Axis:** [[Vector-Store]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.03927) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.03927/paper.pdf)

## Core idea
Two open-source Rust ANN libraries that factor vector representation, distance, quantizer and index independently; HNSW/IVF indexes generic over dense/sparse/multi-vector, matching or beating Faiss on memory-throughput trade-offs.

## Results
> "our Product Quantization matches Faiss in accuracy at competitive speed, our RaBitQ and HNSW match or outperform their reference implementations, and our IVF outperforms Faiss."…

## Rubric
A 1 · B 2 · C 2 · D 2 · E 1 — ANN index layer sits under the Vector-Store axis; B=2 six dense + five sparse systems on seven collections; C=2 open-source Rust; D=2 CPU-only; E=1 would need a

## Relevance for RAG-NIMBF
Candidate for the **Vector-Store** axis at the weekly fit check.

## Status log
- 2026-11-04 screened
