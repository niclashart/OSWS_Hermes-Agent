---
id: hf-caveman-so_trim-1
title: "caveman-so/trim-1"
authors: [caveman-so]
year: 2026
score: 8
rubric: {A: 2, B: 1, C: 2, D: 2, E: 1}
axis: [New-Techniques]
status: fit
screened: 2026-11-01
source: https://huggingface.co/caveman-so/trim-1
pdf: 
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-caveman-so_trim-1/summary.md
tags: [rag-radar, New-Techniques]
---
# caveman-so/trim-1

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [HF](https://huggingface.co/caveman-so/trim-1) · [Summary](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-caveman-so_trim-1/summary.md)

## Core idea
1.2 MB LightGBM context compressor: scores each line of a context against the query (67 features: BM25, line-kind, position, neighbours) and keeps only needed lines verbatim — milliseconds on CPU, deterministic, fails closed.

## Results
> "It saves the most on long-document retrieval, where it removes most of the input and keeps the evidence." (model card)

## Rubric
A 2 · B 1 · C 2 · D 2 · E 1 — context compression / token-budget selection, a technique RAG-NIMBF explicitly cannot express; holdout evidence-kept/cut numbers but no end-to-end RAG answer quality; apache-2.0; new component.

## Relevance for RAG-NIMBF
New axis needed: context compression / selection under a token budget between retrieval and prompt (candidate for `new-axis.md`).

## Status log
- 2026-11-01 screened (HF model: no PDF)
- 2026-11-02 fit-check (W45): not expressible (context compression) → proposals/hf-caveman-so_trim-1/new-axis.md; status fit
