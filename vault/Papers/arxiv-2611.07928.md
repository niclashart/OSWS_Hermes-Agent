---
id: arxiv-2611.07928
title: "ZeroRAG: Adaptive Semantic Peer Routing for Decentralized Retrieval-Augmented Generation"
authors: [Petru Neague, Quinten Stokkink, Martijn de Vos, Rafael Pires, Mathis Randl, Anne-Marie Kermarrec, Johan Pouwelse]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 1, E: 0}
axis: [New-Techniques]
status: rejected
screened: 2026-11-07
source: https://arxiv.org/abs/2611.07928
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.07928/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.07928/summary.md
tags: [rag-radar, new-techniques]
---
# ZeroRAG: Adaptive Semantic Peer Routing for Decentralized RAG

**Axis:** [[New-Techniques]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.07928) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.07928/paper.pdf)

## Core idea
Decentralized retrieval layer: documents stay with owning peers; queries take a best-first walk over a self-organizing semantic overlay (no DHT, no central coordinator); recall improves as the network rewires toward semantically relevant neighbors.

## Results
> "99% of queries locate the best supporting document in at most 13 peer contacts" and ZeroRAG "approaches the recall and end-to-end RAG answer accuracy of a centralized document store, without any global index" (Sec. 4/Summary); "scales to 100 000 peers" (Abstract).

## Rubric
A 2 · B 2 · C 1 · D 1 · E 0 — decentralized multi-peer topology, framework redesign to benchmark.

## Relevance for RAG-NIMBF
Not expressible — would need a peer-network retrieval adapter; candidate for `new-axis.md` at weekly fit check.

## Status log
- 2026-11-07 screened
- 2026-11-09 fit check: rejected — decentralized P2P RAG, E=0 — outside single-node benchmark scope
