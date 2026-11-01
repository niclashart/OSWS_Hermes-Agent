---
id: hf-nvidia_Nemotron-3.5-Rerank-8B-BF16
title: "nvidia/Nemotron-3.5-Rerank-8B-BF16"
authors: [NVIDIA]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [Reranking]
status: screened
screened: 2026-11-01
source: https://huggingface.co/nvidia/Nemotron-3.5-Rerank-8B-BF16
pdf: 
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-nvidia_Nemotron-3.5-Rerank-8B-BF16/summary.md
tags: [rag-radar, Reranking]
---
# nvidia/Nemotron-3.5-Rerank-8B-BF16

**Axis:** [[Reranking]] · **Score:** 8/10 · [HF](https://huggingface.co/nvidia/Nemotron-3.5-Rerank-8B-BF16) · [Summary](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-nvidia_Nemotron-3.5-Rerank-8B-BF16/summary.md)

## Core idea
8B cross-encoder reranker (Ministral-3-8B base) for multilingual (34 languages incl. German) and multimodal retrieval: reranks text, page images, or both — SOTA on ViDoRe v3.1 Reranking.

## Results
> "Nemotron-3.5-Rerank-8B-BF16 achieves state-of-the-art results on the new ViDoRe v3.1 Reranking leaderboard as of October 20, 2026." (model card)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — SOTA on a public leaderboard, 34-language text reranking incl. German; OpenMDW-1.1 license (permissive but not MIT/Apache); multimodal logit reranker → new provider (E 1).

## Relevance for RAG-NIMBF
Not expressible today: RAG-NIMBF rerankers must be sentence-transformers `CrossEncoder`; multimodal/page-image reranking = new provider.

## Status log
- 2026-11-01 screened (HF model: no PDF, mteb link present)
