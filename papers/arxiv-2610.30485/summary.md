# Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences

- **arXiv:** https://arxiv.org/abs/2610.30485
- **Score:** 7/10 (A: 2, B: 2, C: 2, D: 2, E: 0) — environment and dataset public (mempabench.com), four memory systems x four LLM backbones, consumer-feasible
- **Axis:** Datasets

## Core idea
Interactive benchmark (MemPABench) for on-policy evaluation of agent memory over interaction preferences: 99 sessions, preference changes over four months, evaluating Mem0/MemOS/simple RAG/file-based memory.

## Key results (verbatim quotes)
> "Retrieval-based systems (i.e. Mem0, MemOS, simple RAG) do not outperform No Memory, while File-based memory improves accuracy but applies preferences beyond relevant contexts" (Abstract)

## RAG-NIMBF relevance
Evaluation dataset covering simple RAG as baseline; needs a new environment adapter - candidate for Datasets/Evaluation extension. Weekly-fit candidate.
