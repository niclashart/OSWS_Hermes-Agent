# SuSi-RAG: A Hybrid Graph RAG for Equipment Maintenance (arxiv-2611.30588)

**Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.30588)

## Core idea
Hybrid Graph RAG for Bosch equipment maintenance: query and each maintenance record are matched by subgraph similarity, targeting complex causal chains and cross-domain synthesis where vector RAG fails. In production on an active Bosch line for 8+ months with an operational feedback loop for updates.

## Results
> "SuSi-RAG improves top-1 retrieval accuracy from 61.5% to 96.2% and expert-rated answer quality from 44.9% to 84.1% against a vector-based baseline" (Abstract)
> "SuSi-RAG has run on an active Bosch production line for more than eight months, handling 10,664 question-answer interactions and demonstrates upper bound answer accuracy of 96.25% (confirmed error rate 3.75%)." (Abstract)

## Rubric
A 2 · B 1 · C 1 · D 1 · E 0 — graph RAG via subgraph similarity; PoC has baselines but domain-specific (manufacturing) and no public code; industrial deployment evidence; KG approach not expressible in RAG-NIMBF.

## Relevance for RAG-NIMBF
New-Techniques: subgraph-similarity graph retrieval; confirms gap for graph/knowledge-graph retrieval axes.

## Status log
- 2026-11-25 screened
