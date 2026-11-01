---
id: hf-VAGOsolutions_SauerkrautLM-MoEdernColBERT-115M
title: "VAGOsolutions/SauerkrautLM-MoEdernColBERT-115M"
authors: [VAGOsolutions]
year: 2026
score: 8
rubric: {A: 2, B: 1, C: 2, D: 2, E: 1}
axis: [Embedding]
status: screened
screened: 2026-11-01
source: https://huggingface.co/VAGOsolutions/SauerkrautLM-MoEdernColBERT-115M
pdf: 
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-VAGOsolutions_SauerkrautLM-MoEdernColBERT-115M/summary.md
tags: [rag-radar, Embedding]
---
# VAGOsolutions/SauerkrautLM-MoEdernColBERT-115M

**Axis:** [[Embedding]] · **Score:** 8/10 · [HF](https://huggingface.co/VAGOsolutions/SauerkrautLM-MoEdernColBERT-115M) · [Summary](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-VAGOsolutions_SauerkrautLM-MoEdernColBERT-115M/summary.md)

## Core idea
Multilingual ColBERT retriever (de/en/es/nl/fr/it/pt, 32k docs) on a new MoE + hash-embedding ModernBERT-style encoder; 115M params (67.4M active), 1,132 docs/s on one GPU.

## Results
> "German retrieval ahead of models up to 5× larger. MKQA de→en 0.731 vs. 0.671 for Qwen3-Embedding-0.6B." (model card)
> "Long documents up to 32k tokens. LongEmbed 90.1, ahead of the 7B–14B models on the public LongEmbed leaderboard." (model card)

## Rubric
A 2 · B 1 · C 2 · D 2 · E 1 — beats Qwen3/granite baselines on German+multilingual retrieval at 1/5 size; vendor-own numbers; apache-2.0; but ColBERT late interaction → new provider (E 1).

## Relevance for RAG-NIMBF
Not expressible today: RAG-NIMBF only supports dense single-vector embedders; late-interaction (ColBERT) retrieval = new provider/adapter.

## Status log
- 2026-11-01 screened (HF model: no PDF, slot `embedding_models: huggingface:VAGOsolutions/SauerkrautLM-MoEdernColBERT-115M`)
