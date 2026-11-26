---
id: arxiv-2611.34188
title: "MINE: A Training-Free Defense against Indirect Prompt Injection via Mutual Information and Embedding Variance"
authors: [Truong Phan, Ngoc-Quan Pham, Dat Quoc Nguyen]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [Reranking]
status: screened
screened: 2026-11-26
source: https://arxiv.org/abs/2611.34188
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.34188/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.34188/summary.md
tags: [rag-radar, security, reranking]
---
# MINE: A Training-Free Defense against Indirect Prompt Injection via Mutual Information and Embedding Variance

**Axis:** [[Reranking]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.34188) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.34188/paper.pdf)

## Core idea
Training-free prompt-injection defense that maximizes query–passage relevance (mutual information / embedding variance) instead of detecting attacks; doubles as a query-conditioned reranker. Introduces the long-context benchmark LC-Inj-SQuAD (~4,032 words/context).

## Results
> "Across all four, MINE achieves the best accuracy–security trade-off among training-free defenses. It is also the only defense that stays usable against a fully adaptive attacker, generalizes to agent tool-call injection, and achieves the lowest inference latency on long contexts." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — new RAG-security technique + benchmark; 4 datasets incl. adaptive attack; code repo license unverified; embedding-based/training-free; needs new guardrail component, not a config slot.

## Relevance for RAG-NIMBF
Guardrail / injection-defense axis does not exist → `new-axis.md` candidate (weekly fit check).

## Status log
- 2026-11-26 screened
