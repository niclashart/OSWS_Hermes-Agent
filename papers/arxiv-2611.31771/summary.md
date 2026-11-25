# SPARQL-Planned Single-Hop Traversal over a Live Knowledge Graph for Multi-Hop QA (arxiv-2611.31771)

**Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.31771)

## Core idea
Interleaves dense retrieval with traversal of a pre-existing external KG (Wikidata). An LLM plans the traversal as SPARQL code generation, but the query is parsed (into a traversal plan) rather than executed — avoiding empty-result failures of raw SPARQL. KG traversal confirms retrieved passages against a reasoning path, restoring precision after high-recall dense seeding.

## Results
> "we reach 62.5 / 75.1 EM/F1 on HotpotQA, 73.5 / 81.0 on 2WikiMultiHopQA, and 37.1 / 50.0 on MuSiQue, ahead of reproduced HippoRAG2, T²RAG, and IRCoT on all three benchmarks" (Abstract)
> "Executing the generated SPARQL instead of parsing it costs up to 11.4 EM, mostly because raw queries return empty results, not because of syntax errors." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 0 — graph-RAG variant with KG grounding; full 1000-question splits, three benchmarks, reproduced baselines, ablation; license CC BY-NC-SA, no code stated; runs with a single configuration; but KG traversal is explicitly not expressible in RAG-NIMBF.

## Relevance for RAG-NIMBF
New-Techniques: external-KG traversal stage (plan-then-parse) as new retrieval component.

## Status log
- 2026-11-25 screened
