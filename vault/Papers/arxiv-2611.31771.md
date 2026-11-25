---
id: arxiv-2611.31771
title: "SPARQL-Planned Single-Hop Traversal over a Live Knowledge Graph for Multi-Hop Question Answering"
authors: [Priyesh Vakharia, Masud Moshtaghi, Pratyay Banerjee]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-11-25
source: https://arxiv.org/abs/2611.31771
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.31771/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.31771/summary.md
tags: [rag-radar, New-Techniques]
---
# SPARQL-Planned Single-Hop Traversal over a Live Knowledge Graph for Multi-Hop QA

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.31771) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.31771/paper.pdf)

## Core idea
Dense retrieval seeds candidates; an LLM plans a Wikidata traversal as SPARQL that is parsed (not executed) into a traversal plan, confirming passages against a KG reasoning path — precision after recall.

## Results
> "we reach 62.5 / 75.1 EM/F1 on HotpotQA, 73.5 / 81.0 on 2WikiMultiHopQA, and 37.1 / 50.0 on MuSiQue, ahead of reproduced HippoRAG2, T²RAG, and IRCoT on all three benchmarks" (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 0 — KG-grounded multi-hop retrieval; full splits, reproduced baselines, ablation (execute vs parse); CC BY-NC-SA, no code; single config; KG traversal not expressible.

## Relevance for RAG-NIMBF
New retrieval component: external-KG traversal (plan-then-parse) stage.

## Status log
- 2026-11-25 screened
