# TopoGraphRAG-Bench: Evaluating Multimodal GraphRAG on Layout-Grounded Evidence Reasoning (2610.09360)

**Score: 7/10** · [arXiv](https://arxiv.org/abs/2610.09360) · screened 2026-10-25

## Core idea
Layout-grounded benchmark for multimodal GraphRAG: 2,024 questions over 201 visually rich documents under three controlled evidence topologies (single-hop, bridge-chain, multi-source synthesis), with counterfactual validation for shortcuts.

## Key results
> "We evaluate text-only GraphRAG, page-level visual retrieval, and multimodal GraphRAG systems using retrieval, generation, and topology-aware reasoning metrics. Multimodal GraphRAG systems achieve the strongest overall performance, but still fail when visual-textual evidence alignment or multi-unit composition is incomplete." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 1 · E 1 = 7 — A2 · B2 · C1 · D1 · E1 — counterfactually validated benchmark, code+data public; multimodal/graph systems need heavy VRAM; GraphRAG not expressible.

## Affected axis
Datasets

## Relevance for RAG-NIMBF
Graph RAG is explicitly not expressible in RAG-NIMBF; the benchmark is a candidate Datasets adapter but the system side needs a new axis → `new-axis.md`.
