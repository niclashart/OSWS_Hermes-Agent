---
id: arxiv-2611.34366
title: "ConTra: A Training Framework for Effective Contextual Retrieval via Prefix Generation"
authors: [SStan1 et al.]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 2, D: 2, E: 1}
axis: [Chunking]
status: screened
screened: 2026-11-26
source: https://arxiv.org/abs/2611.34366
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.34366/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.34366/summary.md
tags: [rag-radar, chunking, contextual-retrieval]
---
# ConTra: A Training Framework for Effective Contextual Retrieval via Prefix Generation

**Axis:** [[Chunking]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.34366) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.34366/paper.pdf) · [Code](https://github.com/SStan1/ConTra)

## Core idea
RL-trained 2B prefix generator writes one contextual prefix per chunk at indexing time; prefixes serve both vector search and reranking. Introduces RealContextBench (5 collections, 3 distractor conditions).

## Results
> "ConTra-2B outperforms the prompted 9B baseline using Anthropic's method and the PPLX-4B contextual encoder, with a margin of up to 3.15 points over their best overall scores, while indexing short documents 7.74 times and 2.15 times as fast as those baselines, respectively." (Abstract)

## Rubric
A 2 · B 2 · C 2 · D 2 · E 1 — contextual chunk prefixes, clear new ingestion option; ConTEB + RealContextBench vs strong baselines; open code/models; 2B generator consumer-GPU feasible; needs ingestion pipeline step beyond `chunking_strategies`.

## Relevance for RAG-NIMBF
Contextual prefix generation at ingestion not expressible → `new-axis.md` candidate (ingestion_method extension).

## Status log
- 2026-11-26 screened
