---
id: hf-VAGOsolutions_SauerkrautLM-MoEdernColBERT-27M
title: "VAGOsolutions/SauerkrautLM-MoEdernColBERT-27M"
authors: [VAGOsolutions]
year: 2026
score: 8
rubric: {A: 2, B: 1, C: 2, D: 2, E: 1}
axis: [Embedding]
status: fit
screened: 2026-11-01
source: https://huggingface.co/VAGOsolutions/SauerkrautLM-MoEdernColBERT-27M
pdf: 
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-VAGOsolutions_SauerkrautLM-MoEdernColBERT-27M/summary.md
tags: [rag-radar, Embedding]
---
# VAGOsolutions/SauerkrautLM-MoEdernColBERT-27M

**Axis:** [[Embedding]] · **Score:** 8/10 · [HF](https://huggingface.co/VAGOsolutions/SauerkrautLM-MoEdernColBERT-27M) · [Summary](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-VAGOsolutions_SauerkrautLM-MoEdernColBERT-27M/summary.md)

## Core idea
27M-param (12.3M active) multilingual ColBERT retriever on MoEdernBERT; 6,708 docs/s on one GPU, 32k-token docs, beats granite-97m everywhere and Qwen3-Embedding-0.6B on German/multilingual MKQA.

## Results
> "German retrieval ahead of models up to 22× larger. MKQA de→en 0.690 vs. 0.671 for Qwen3-Embedding-0.6B." (model card)
> "4.3× the throughput of granite-97m-multilingual-r2 and 47× that of Qwen3-Embedding-0.6B: 6,708 documents per second on one GPU." (model card)

## Rubric
A 2 · B 1 · C 2 · D 2 · E 1 — strong German/multilingual quality at 1/22 size and very high throughput; vendor numbers; apache-2.0; ColBERT → E 1.

## Relevance for RAG-NIMBF
Not expressible today (late-interaction embedder → new provider; candidate for `new-axis.md` in weekly fit check).

## Status log
- 2026-11-01 screened (HF model: no PDF, slot `embedding_models: huggingface:VAGOsolutions/SauerkrautLM-MoEdernColBERT-27M`)
- 2026-11-02 fit-check (W45): not expressible (late-interaction embedder) → proposals/hf-VAGOsolutions_SauerkrautLM-MoEdernColBERT-27M/new-axis.md; status fit
