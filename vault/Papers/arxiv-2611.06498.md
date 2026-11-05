---
id: arxiv-2611.06498
title: "Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap in Offline Retrieval-Augmented Generation"
authors: [Georgios Feretzakis, Alexandros Papaspyridis]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 2, D: 2, E: 1}
axis: [Vector-Store]
status: screened
screened: 2026-11-05
source: https://arxiv.org/abs/2611.06498
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.06498/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.06498/summary.md
tags: [rag-radar, Vector-Store]
---
# Signed but Steerable (Text-Vector Integrity Gap)

**Axis:** [[Vector-Store]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.06498) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.06498/paper.pdf)

## Core idea
Signatures on offline RAG knowledge packs prove the publisher, not that stored vectors encode the signed text. The "margin law" ties the attacker's query-hijack rate to angular retrieval margins at the verifier's cosine tolerance; exact verification of quantisation codes with a guard band closes the gap without rejecting honest vectors.

## Results
> "on a Raspberry Pi 5 running a local language model, such an attack lowers correct answers from 0.75 to 0.39" (Abstract / Sec. 5.5)
> "Verifying quantisation codes instead ... accepted every honest vector in our samples on three platforms and left the publisher no choice" (Abstract)

## Rubric
A 2 · B 2 · C 2 · D 2 · E 1 — new vector-store security technique; 5 corpora/2 embedders/device E2E; code+data public; Pi-5 feasible; needs a new integrity-check component.

## Relevance for RAG-NIMBF
Not a config value today: an integrity/tamper benchmark stage over [[Vector-Store]] backends would be needed (new component + metric).

## Status log
- 2026-11-05 screened
