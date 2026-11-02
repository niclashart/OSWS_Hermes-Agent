---
id: arxiv-2610.41172
title: "Context as Infrastructure: Knowledge Compilation for Retrieval in Agentic Systems with Harnesses"
authors: [et al.]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 2, D: 1, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-11-02
source: https://arxiv.org/abs/2610.41172
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.41172/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.41172/summary.md
tags: [rag-radar, New-Techniques]
---
# Context as Infrastructure: Knowledge Compilation for Retrieval in Agentic Systems with Harnesses

**Axis:** [[New-Techniques]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2610.41172) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.41172/paper.pdf)

## Core idea
Agentic retrieval harnesses have solved accuracy (85% BrowseComp-Plus, 91% FRAMES with BM25+grep only); the bottleneck is context supply. Knowledge compilation at ingestion (claim–evidence navigation trees, graphs, timelines; implemented in RAGFlow) cuts tokens, not errors.

## Results
> "cuts total query tokens by 91% when the evidence suffices and adds 1.9% when it does not, for a 38% average reduction" (Sec. 4)
> "the decision gate reduced mean end-to-end latency from 140 s to 30 s" (Sec. 8.5)

## Rubric
A 2 · B 2 · C 2 · D 1 · E 0 — context compilation + harness loop both need new components; not expressible in RAG-NIMBF.

## Relevance for RAG-NIMBF
Needs new axis: ingestion-side compilation artifacts + agent context budget / decision gate. Candidate for `new-axis.md` in the weekly fit check.

## Status log
- 2026-11-02 screened
