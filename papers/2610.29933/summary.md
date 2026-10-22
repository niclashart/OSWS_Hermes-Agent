# ThreadRAG — Graph Topology Meets Energy-Driven Pathfinding (arXiv:2610.29933)

## Core idea
Graph-RAG framework that avoids semantic loss of triplet-style KGs: a Semantic Topology Mapper organises retrieved documents into context-intact Semantic Nodes and builds a Semantic Topology Graph with narrative, semantic, and lexical edges; Energy-Driven Pathfinding selects query-relevant subgraphs via energy diffusion and linearises them deterministically into coherent textual evidence paths.

## Results
> "it achieves a 14.4% EM improvement over text-centric methods on HotpotQA and surpasses the best baseline by 5.8% EM on 2WikiMultihop, while reducing token cost to 23.3% of the strongest baseline" (Abstract; three multi-hop QA benchmarks; Findings of EMNLP 2026).

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — clear new graph-RAG technique; 3 benchmarks, strong baselines; code not explicitly open; runs with open LLMs; graph pipeline is a new component, not a config value.

## Relevance for RAG-NIMBF
Graph RAG is not expressible today (see nimbf-capabilities "Not expressible"). Candidate for a new `graph` axis / RAG-System adapter.
