---
id: hf-opensearch-project_opensearch-neural-embed-v1
title: "opensearch-project/opensearch-neural-embed-v1"
authors: [OpenSearch Project]
year: 2026
score: 10
rubric: {A: 2, B: 2, C: 2, D: 2, E: 2}
axis: [Embedding]
status: screened
screened: 2026-11-13
source: https://huggingface.co/opensearch-project/opensearch-neural-embed-v1
pdf:
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-opensearch-project_opensearch-neural-embed-v1/summary.md
tags: [rag-radar, Embedding]
---
# opensearch-project/opensearch-neural-embed-v1

**Axis:** [[Embedding]] · **Score:** 10/10 · [HF](https://huggingface.co/opensearch-project/opensearch-neural-embed-v1) · [MTEB results](https://github.com/embeddings-benchmark/results/tree/main/results/opensearch-project__opensearch-neural-embed-v1)

## Core idea
598M English dense embedder (2048-dim), distilled without labeled data from two teachers into a Qwen3-Embedding-0.6B student; Apache-2.0, sentence-transformers loadable.

## Results
> "ranks #1 among single-vector dense models under 1B parameters on the MTEB BEIR benchmark (58.37 average NDCG@10 over 15 tasks) and #2 among models under 1B parameters on MTEB(eng, v2) (73.76 Mean (Task)), within 1.5 points of the nearly 13x larger Qwen3-Embedding-8B." (model card)

## Rubric
A 2 · B 2 · C 2 · D 2 · E 2 — BEIR #1 <1B beats models users already run; public MTEB results; Apache-2.0; drop-in slot value.

## Relevance for RAG-NIMBF
Ready-to-use slot: `embedding_models: huggingface:opensearch-project/opensearch-neural-embed-v1` (one-axis experiment vs. current default embedder).

## Status log
- 2026-11-13 screened (HF model: no PDF, mteb link present)
