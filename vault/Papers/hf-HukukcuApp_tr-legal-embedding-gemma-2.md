---
id: hf-HukukcuApp_tr-legal-embedding-gemma-2
title: "HukukcuApp/tr-legal-embedding-gemma-2"
authors: [HukukcuApp]
year: 2026
score: 7
rubric: {A: 1, B: 1, C: 1, D: 2, E: 2}
axis: [Embedding]
status: screened
screened: 2026-11-01
source: https://huggingface.co/HukukcuApp/tr-legal-embedding-gemma-2
pdf: 
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-HukukcuApp_tr-legal-embedding-gemma-2/summary.md
tags: [rag-radar, Embedding]
---
# HukukcuApp/tr-legal-embedding-gemma-2

**Axis:** [[Embedding]] · **Score:** 7/10 · [HF](https://huggingface.co/HukukcuApp/tr-legal-embedding-gemma-2) · [Summary](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-HukukcuApp_tr-legal-embedding-gemma-2/summary.md)

## Core idea
Turkish legal-domain dense retriever (271M, embeddinggemma-2 base) fine-tuned on 118k Yargıtay case-law triplets with BM25 hard-negative mining for precedent retrieval.

## Results
> "118.078 adet içtihadi üçlü (triplet) ile fine-tune edilmiştir" (model card) — no named baselines in the card.

## Rubric
A 1 · B 1 · C 1 · D 2 · E 2 — domain-specific single non-English (non-German) language → A max 1; Gemma license; sentence-transformers-loadable.

## Relevance for RAG-NIMBF
Expressible (`embedding_models: huggingface:HukukcuApp/tr-legal-embedding-gemma-2`) but no Turkish dataset in RAG-NIMBF; unlikely fit-check candidate.

## Status log
- 2026-11-01 screened (HF model: no PDF)
