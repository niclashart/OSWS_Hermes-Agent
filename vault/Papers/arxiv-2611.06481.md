---
id: arxiv-2611.06481
title: "ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs"
authors: [Jyotin Goel, Abhinav Arun, Tejas Prakash Agarwal]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 1, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-11-05
source: https://arxiv.org/abs/2611.06481
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.06481/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.06481/summary.md
tags: [rag-radar, New-Techniques]
---
# ArcRAG

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.06481) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.06481/paper.pdf)

## Core idea
Query-local graph interface induction at inference time lets one construction-agnostic retriever (explore → plan → Cypher with repair) work across different knowledge-graph constructions (schema-guided vs open-IE) of MuSiQue/HotpotQA/TriviaQA without retuning.

## Results
> "query-time interface induction keeps a construction-agnostic retriever effective when the construction changes, although construction still shapes absolute accuracy" (Abstract / Sec. 6.2)

## Rubric
A 2 · B 2 · C 1 · D 1 · E 0 — agentic graph retrieval; 3 datasets + ablations; CC BY-NC-ND, code unclear; LLM-planned multi-hop moderate; Graph RAG not expressible.

## Relevance for RAG-NIMBF
Graph RAG remains in the not-expressible list; candidate for a future graph-retrieval axis.

## Status log
- 2026-11-05 screened
