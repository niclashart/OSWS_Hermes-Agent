---
id: hf-f4roukb_denserepr-code-48M-pretrain-EN-v1
title: "denserepr-code-48M-pretrain-EN-v1 (48M code-retrieval embedder)"
authors: [f4roukb]
year: 2026
score: 10
rubric: {A: 2, B: 2, C: 2, D: 2, E: 2}
axis: [Embedding]
status: proposed
screened: 2026-11-18
source: https://huggingface.co/f4roukb/denserepr-code-48M-pretrain-EN-v1
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-f4roukb_denserepr-code-48M-pretrain-EN-v1/summary.md
tags: [rag-radar, Embedding]
---
# denserepr-code-48M-pretrain-EN-v1

**Axis:** [[Embedding]] · **Score:** 10/10 · [Model card](https://huggingface.co/f4roukb/denserepr-code-48M-pretrain-EN-v1)

## Core idea
48M-param dense embedder for code retrieval (384-d, 8k context, apache-2.0, sentence-transformers),
made by continued contrastive pretraining of granite-embedding-small-english-r2 on ~23M code pairs.

## Results
> "It scores **64.84 mean nDCG@10 on CoIR** (10 tasks), +11.4 over the model it was trained from." (model card)

Best dense single-vector model on MTEB CoIR; only CosQA regresses (35.40 → 33.84).

## Rubric
A 2 · B 2 · C 2 · D 2 · E 2 — SOTA dense on MTEB CoIR at tiny size; MTEB-measured with base baseline;
apache-2.0; runs anywhere; `SentenceTransformer`-loadable.

## Relevance for RAG-NIMBF
`embedding_models: huggingface:f4roukb/denserepr-code-48M-pretrain-EN-v1` — direct axis value for
code-RAG experiments; compare against current default embedder (one-axis change).

## Status log
- 2026-11-18 screened
- 2026-11-23 weekly fit: proposed
