# ConTra: A Training Framework for Effective Contextual Retrieval via Prefix Generation

**Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.34366) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.34366/paper.pdf)

## Core idea
RL-trained lightweight prefix generators (ConTra-2B) that write one contextual prefix per chunk at indexing time; reward combines frozen embedder + reranker feedback with factual verification and length control. Prefixes serve both vector search and reranking. Also introduces RealContextBench (5 collections, 3 distractor conditions).

## Results
> "ConTra-2B outperforms the prompted 9B baseline using Anthropic's method and the PPLX-4B contextual encoder, with a margin of up to 3.15 points over their best overall scores, while indexing short documents 7.74 times and 2.15 times as fast as those baselines, respectively." (Abstract)
> "Code, datasets, and trained models are available at https://github.com/SStan1/ConTra." (Abstract)

## Rubric
A 2 · B 2 · C 2 · D 2 · E 1 — clear new chunking/indexing option (contextual chunk prefixes) (A); ConTEB + RealContextBench vs strong baselines (B); public code/datasets/models (C); 2B generator, consumer-GPU feasible at index time (D); needs a new ingestion pipeline step (prefix generation + storing augmented text+embedding) — not a plain chunker config value (E).

## Relevance for RAG-NIMBF
Not expressible today: contextual chunk prefixes at ingestion are beyond `chunking_strategies`; needs ingestion_method extension or new axis. Candidate for `new-axis.md`.

## Status log
- 2026-11-26 screened
