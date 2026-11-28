---
id: hf-FrontiersMind_EmbeddingNandi-150M
title: "FrontiersMind/EmbeddingNandi-150M"
authors: [FrontiersMind]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 2, D: 2, E: 2}
axis: [Embedding]
status: screened
screened: 2026-11-28
source: https://huggingface.co/FrontiersMind/EmbeddingNandi-150M
pdf: 
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-FrontiersMind_EmbeddingNandi-150M/summary.md
tags: [rag-radar, Embedding]
---
# FrontiersMind/EmbeddingNandi-150M

**Axis:** [[Embedding]] · **Score:** 8/10 · [HF](https://huggingface.co/FrontiersMind/EmbeddingNandi-150M) · [Summary](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-FrontiersMind_EmbeddingNandi-150M/summary.md)

## Core idea
146M Apache-2.0 embedder: English + 13 Indic languages + Arabic/Indonesian/Malay, 16K-token window (long docs without chunking), Matryoshka to 128–768 dims; slot line `embedding_models: huggingface:FrontiersMind/EmbeddingNandi-150M`.

## Results
> "Average is the mean of the three benchmark scores" — MTEB(eng,v2) 65.85 / MTEB(Code,v1) 75.80 / MTEB(Indic,v1) 74.33, avg 71.99 vs UltraBERT-Embed-150M 60.90 and granite-embedding-english-r2 50.97. (model card, Benchmark Results)

## Rubric
A 2 · B 2 · C 2 · D 2 · E 2 — clear capability add (long context + multilingual at 146M) with MTEB baselines; Apache-2.0; sentence-transformers loadable → slot-ready.

## Relevance for RAG-NIMBF
Directly expressible: `embedding_models: huggingface:FrontiersMind/EmbeddingNandi-150M` (needs `trust_remote_code`; note weak English-retrieval score 49.75 on MTEB eng v2).

## Status log
- 2026-11-28 screened (HF model: no PDF, mteb link absent)
