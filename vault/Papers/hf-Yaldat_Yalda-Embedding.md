---
id: hf-Yaldat_Yalda-Embedding
title: "Yaldat/Yalda-Embedding"
authors: [Yaldat]
year: 2026
score: 7
rubric: {A: 1, B: 2, C: 2, D: 2, E: 2}
axis: [Embedding]
status: proposed
screened: 2026-11-09
source: https://huggingface.co/Yaldat/Yalda-Embedding
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-Yaldat_Yalda-Embedding/summary.md
tags: [rag-radar, Embedding, persian]
---
# Yaldat/Yalda-Embedding

**Axis:** [[Embedding]] · **Score:** 7/10 · [Model card](https://huggingface.co/Yaldat/Yalda-Embedding)

## Core idea
Persian dense-retrieval embedder, fine-tuned from Qwen3-Embedding-0.6B on >1M Persian query-document pairs with relational knowledge distillation from F2LLM-v2-8B. 595.8M params, 1024-dim, Apache 2.0, sentence-transformers loadable.

## Results
> "Yalda achieves **state-of-the-art performance among the evaluated 0.6B models** on eight Persian retrieval tasks from FaMTEB. Its reported mean is **0.5488**, compared with **0.4713** for its Qwen3-0.6B initialization and **0.5563** for Qwen3-Embedding-4B." (Model card)

## Rubric
A 1 · B 2 · C 2 · D 2 · E 2 — domain fine-tune (Persian) caps A at 1; clear gain over its base model; slot-ready.

## Relevance for RAG-NIMBF
Ready-to-use slot value: `embedding_models: huggingface:Yaldat/Yalda-Embedding` (one-axis comparison vs. current default).

## Status log
- 2026-11-09 screened
- 2026-11-09 fit check: expressible (E=2) — proposal config.yaml on proposal/2026-W46
