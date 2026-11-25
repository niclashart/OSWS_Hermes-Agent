---
id: hf-harims95_hobbylm-embed-140m
title: "hobbylm-embed-140m (sparse MoE embedder, 140M, Apache-2.0)"
authors: [Fuel Labs / harims95]
year: 2026
score: 7
rubric: {A: 1, B: 2, C: 2, D: 2, E: 2}
axis: [Embedding]
status: screened
screened: 2026-11-25
source: https://huggingface.co/harims95/hobbylm-embed-140m
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-harims95_hobbylm-embed-140m/summary.md
tags: [rag-radar, Embedding]
---
# hobbylm-embed-140m

**Axis:** [[Embedding]] · **Score:** 7/10 · [HF](https://huggingface.co/harims95/hobbylm-embed-140m) · [MTEB](https://github.com/embeddings-benchmark/results/tree/main/results/harims95__hobbylm-embed-140m)

## Core idea
140M-param sparse-MoE English embedder trained from scratch; 512-d dense output; sentence-transformers + GGUF/Ollama; Apache-2.0.

## Results
> "62.33 on MTEB(eng, v2), all 41 tasks" (model card)

## Rubric
A 1 · B 2 · C 2 · D 2 · E 2 — no demonstrated win over existing defaults; official MTEB; open license; tiny; loadable via SentenceTransformer.

## Relevance for RAG-NIMBF
`embedding_models: huggingface:harims95/hobbylm-embed-140m`

## Status log
- 2026-11-25 screened
