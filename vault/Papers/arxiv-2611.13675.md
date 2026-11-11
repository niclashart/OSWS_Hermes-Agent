---
id: arxiv-2611.13675
title: "OpticalRAG: Pixel-Space Compression for Token-Efficient Retrieval-Augmented Generation"
authors: [Senhao Liu, ...]
year: 2026
score: 9
rubric: {A: 2, B: 2, C: 2, D: 1, E: 2}
axis: [New-Techniques]
status: screened
screened: 2026-11-11
source: https://arxiv.org/abs/2611.13675
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.13675/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.13675/summary.md
tags: [rag-radar, New-Techniques]
---
# OpticalRAG: Pixel-Space Compression for Token-Efficient Retrieval-Augmented Generation

**Axis:** [[New-Techniques]] · **Score:** 9/10 · [arXiv](https://arxiv.org/abs/2611.13675) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.13675/paper.pdf)

## Core idea
Compresses retrieved documents in pixel space: render pages as images, encode with a frozen vision encoder, retrieve visual tokens via a text-to-visual projection, distill into 16 query-conditioned prefix tokens for the LLM.

## Results
> "OpticalRAG achieves the best compression-aware accuracy (CAP) on all three benchmarks while injecting only $16$ tokens, and improves the closed-book Qwen2.5-7B-Instruct backbone by $5.17$ points on LongBench-v2." (Abstract)

## Rubric
A 2 · B 2 · C 2 · D 1 · E 2 — new compression modality, 3 benchmarks vs strong baselines, MIT code+weights, needs frozen DeepSeek-OCR encoder + 7B LLM.

## Relevance for RAG-NIMBF
Context compression / selection under token budget is not expressible today → New-Techniques.

## Status log
- 2026-11-11 screened
