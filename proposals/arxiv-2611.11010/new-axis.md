# New-axis proposal — arXiv:2611.11010

**Paper:** "Lightfoot: Graph Retrieval-Augmented Generation with Exact, Model-Free Document Deletion" (arXiv:2611.11010) — vault note [[arxiv-2611.11010]], screened 2026-11-11, score 8/10.

## What the paper shows
GraphRAG with chunk-level provenance making document deletion a pure DB operation. Quotes (Abstract): "Lightfoot builds the cheapest index on all three datasets, 26-31% below HippoRAG 2 and 3-6x below LightRAG and fast-graphrag"; "after deleting 10% of the documents, the graph is identical to a fresh index of the surviving documents."

## Why not expressible in RAG-NIMBF today
Graph RAG / knowledge-graph retrieval is explicitly listed as not expressible. Beyond the missing graph adapter, the paper introduces *lifecycle properties* RAG-NIMBF cannot measure at all: index build cost per passage and a deletion-correctness invariant (graph-after-delete ≡ fresh index) — no such stage or metric exists.

## What RAG-NIMBF would need
- `rag_system_adapter: graph-*` (or a graph plugin) covering ingestion (per-passage extraction), PPR retrieval, local reranking.
- Lifecycle metrics: index build cost (LLM calls, $, tokens), deletion test (graph isomorphism or hash comparison after delete vs. fresh index).
- Multi-hop datasets (MuSiQue, HotpotQA, 2WikiMultiHopQA) as `hf-generic`/new adapters.

## Estimated effort
Large (~2–3 weeks): graph adapter + ingestion pipeline + two new metric families. Full-corpus setups need >24 GB GPU, so benchmark at reduced corpus scale.
