---
id: hf-dotproductx_breadbowl-embed-v1.3
title: "dotproductx/breadbowl-embed-v1.3"
authors: [BreadBowlAI]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 2, D: 1, E: 1}
axis: [Embedding, Reranking, New-Techniques]
status: screened
screened: 2026-11-27
source: https://huggingface.co/dotproductx/breadbowl-embed-v1.3
pdf: ""
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-dotproductx_breadbowl-embed-v1.3/summary.md
tags: [rag-radar, Embedding, Reranking]
---
# breadbowl-embed-v1.3

**Axis:** [[Embedding]] / [[Reranking]] · **Score:** 8/10 · [Model card](https://huggingface.co/dotproductx/breadbowl-embed-v1.3) · [Code](https://github.com/BreadBowlAI/breadbowl-embed)

## Core idea
Late-interaction slot model (Qwen3.5-0.8B backbone, 755M params, Apache-2.0): passages encoded once into 16 routing/value slot pairs; routing vectors find candidates, value vectors rerank by attention over stored values — no second model pass at query time. Replaces embedder + cross-encoder with one model.

## Results
> "Level with Qwen3-Embedding-0.6B + Qwen3-Reranker-0.6B on MS MARCO and DL19, and 5.5 nDCG@10 ahead on DL20."

> "50× faster rerank. 2.9 ms against 150 ms on the same candidates."

> "BEIR: 55.1 mean over 15 tasks" (self-reported; MS MARCO dev nDCG@10 41.71, Recall@100 84.46)

## Rubric
A 2 · B 2 · C 2 · D 1 · E 1 — beats a stack users already run; full-corpus BEIR baselines; Apache-2.0 weights+code; CUDA path unvalidated; late-interaction slot model not sentence-transformers loadable (E 1 per rubric).

## Relevance for RAG-NIMBF
Not slot-ready: needs a new provider (custom index over routing/value vectors) — a `New-Techniques` candidate combining the Embedding and Reranking axes.

## Status log
- 2026-11-27 screened
