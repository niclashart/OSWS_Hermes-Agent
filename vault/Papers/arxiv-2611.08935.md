---
id: arxiv-2611.08935
title: "SkinMind: Equipping Agentic RAG with Human-Inspired Graph Probing for Reliable Dermatology AI"
authors: [Jing Hao, Weinan Zhou]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 0, D: 0, E: 1}
axis: [RAG-System]
status: rejected
screened: 2026-11-09
source: https://arxiv.org/abs/2611.08935
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.08935/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.08935/summary.md
tags: [rag-radar, RAG-System, agentic, graph]
---
# SkinMind: Agentic RAG with Graph Probing

**Axis:** [[RAG-System]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.08935) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.08935/paper.pdf)

## Core idea
Agentic RAG that iteratively probes a dermatology knowledge graph via eight tools, building query-specific evidence subgraphs; +8.7/+8.9 points over direct answering across six VQA benchmarks.

## Results
> "SkinMind improves the average score over direct answering by 8.70 and 8.89 points with GPT-5.4-mini and Gemini-2.5-Flash, respectively" (Abstract)

## Rubric
A 2 · B 2 · C 0 · D 0 · E 1 — no code/weights, CC BY-NC-ND, proprietary APIs only; graph retrieval not expressible.

## Relevance for RAG-NIMBF
Graph RAG → [[New-Techniques]]; nearest existing mechanism is the MCP agentic adapter.

## Status log
- 2026-11-09 screened
- 2026-11-09 fit check: rejected — dermatology graph-probing RAG, CC BY-NC-ND + no code — license blocks reuse, domain-specific
