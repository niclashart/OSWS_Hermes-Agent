# 2610.38366 — TCC-RAG: Temporal Causal Chain-Guided RAG for Temporal Knowledge Graph Question Answering

**Score:** 7/10 · **Axis:** New-Techniques · [arXiv](https://arxiv.org/abs/2610.38366) · [HTML](https://arxiv.org/html/2610.38366)

## Core idea
TCC-RAG reformulates a temporal knowledge graph into a multi-view causal cue graph, builds a query-specific temporal causal chain to guide retrieval, and applies a causal evidence filter so only causally consistent knowledge reaches the LLM.

## Key results (verbatim quotes)
> "TCC-RAG achieves substantial performance gains of 10.72% and 8.40% on two TKGQA benchmarks, and delivers a remarkable 62.97% improvement for multi-step temporal reasoning." (Abstract)

## Rubric score with justification
A 2 (causal-chain graph RAG; new technique) · B 2 (two TKGQA benchmarks, large multi-step gains) · C 0 (no code released) · D 1 (LLM-scale unclear) · E 0 (graph construction + guided retrieval not expressible)

## Affected axis
New-Techniques: New technique: causal-cue graph retrieval for temporal KGQA — squarely in the graph-RAG gap. Evidence strong but C=0 limits reproduction; new-axis.md candidate.
