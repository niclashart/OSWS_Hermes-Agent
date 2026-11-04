# EAGR: Evidence-Guided Adaptive Graph Retrieval

- arXiv: https://arxiv.org/abs/2611.01910
- Screened: 2026-11-04 · Score: 7/10 · Rubric A-E: (2, 2, 1, 2, 0)
- Axis: New-Techniques

## Core idea
Adaptive multi-hop retrieval over an implicit semantic graph in a plain VectorDB: an LLM assesses accumulated evidence, expands the frontier via metadata neighborhood lookup, and terminates when sufficient — no GraphDB, no query rewriting.

## Key results (verbatim quotes)
> "EAGR achieves the highest LLM-based answer accuracy among evaluated methods, outperforming the vanilla RAG by 17% and strongest graph-aware baseline by 4% percentage points averaged across three popular benchmarks HotPotQA, 2WikiMultiHopQA, and MuSiQue." (Abstract)

## Rubric justification
A=2: evidence-guided adaptive retrieval loop; B=2 three multi-hop benchmarks; C=1 no code mentioned; D=2 LLM-driven, standard VectorDB; E=0: adaptive frontier-expansion loop not expressible in RAG-NIMBF config.

## RAG-NIMBF relevance
Not expressible as a single config value — new technique (see New-Techniques / New-Techniques).
