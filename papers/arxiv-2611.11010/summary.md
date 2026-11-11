# Lightfoot: Graph Retrieval-Augmented Generation with Exact, Model-Free Document Deletion

arXiv 2611.11010 · CC BY 4.0 · code: https://github.com/udayallu-ml/Lightfoot-GraphRAG

## Core idea
GraphRAG where every entity/link/fact/synonym edge is a deterministic function of per-passage extractions with chunk-level provenance. Indexing costs one LLM call per passage, retrieval none (fact-seeded Personalized PageRank + local cross-encoder), and document deletion is a pure database operation that provably reproduces a fresh index.

## Key results (verbatim)
> "On the full 11,402-passage MuSiQue corpus we verify that, after deleting 10% of the documents, the graph is identical to a fresh index of the surviving documents." (Abstract)

> "Lightfoot builds the cheapest index on all three datasets, 26-31% below HippoRAG 2 and 3-6x below LightRAG and fast-graphrag." (Abstract)

> "Against HippoRAG 2 it is significantly better on MuSiQue retrieval (+2.8 points recall@5 and +4.3 recall@10 on a held-out split) and on HotpotQA answers (+7.7 points exact match), and significantly worse on 2WikiMultiHopQA (-3.9 recall@2, -8.4 F1)." (Abstract)

## Rubric
A 2 · B 2 · C 2 · D 1 · E 1 — 8/10 → relevant. New benchmarkable properties (index cost, deletion correctness) for graph RAG; 3 multi-hop datasets, strong baselines, significance tests; open code; graph RAG itself needs >24 GB setup for full corpora; graph RAG not expressible in RAG-NIMBF → new component + new metrics.

## Affected axis
New-Techniques — graph RAG plus lifecycle metrics (index cost, deletion invariant) are absent from RAG-NIMBF.

## Status log
- 2026-11-11 screened
