---
id: arxiv-2611.30335
title: "MH-RAG-DIVE: Dynamic and Cost-Efficient Multi-Hop RAG Evaluation via Tree-Cached Dialogue Simulation"
authors: [Lorenz Brehme, Daniel Hillebrand, Thomas Ströhle, Ruth Breu]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 2, D: 2, E: 0}
axis: [Evaluation]
status: screened
screened: 2026-11-25
source: https://arxiv.org/abs/2611.30335
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.30335/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.30335/summary.md
tags: [rag-radar, Evaluation]
---
# MH-RAG-DIVE: Dynamic and Cost-Efficient Multi-Hop RAG Evaluation via Tree-Cached Dialogue Simulation

**Axis:** [[Evaluation]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.30335) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.30335/paper.pdf) · [Code](https://github.com/Daniel-Innsbruck/MH-RAG-DIVE)

## Core idea
Dynamic user-simulation evaluation for multi-hop multi-turn RAG: a Context Discoverer generates multi-hop questions from combinable documents mid-conversation; a Conversation Cacher reuses turns across runs to cut cost.

## Results
> "the Conversation Cacher substantially reduces token consumption, demonstrating its potential to make dynamic evaluation more cost-efficient." (Abstract)

## Rubric
A 2 · B 2 · C 2 · D 2 · E 0 — new evaluation protocol; six RAG configs, RAG-DIVE + CLAPNQ comparison, industrial case; CC-BY code+data; dynamic simulation not expressible by static dataset adapters.

## Relevance for RAG-NIMBF
Would need a new dynamic-evaluation dataset-adapter type (simulated user + caching).

## Status log
- 2026-11-25 screened
