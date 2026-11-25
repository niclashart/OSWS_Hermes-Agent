# MH-RAG-DIVE: Dynamic and Cost-Efficient Multi-Hop RAG Evaluation via Tree-Cached Dialogue Simulation (arxiv-2611.30335)

**Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.30335)

## Core idea
Dynamic interactive user-simulation evaluation for RAG in multi-hop, multi-turn settings. Extends RAG-DIVE with a Context Discoverer (finds combinable documents to generate multi-hop questions mid-conversation) and a Conversation Cacher that reuses turns from previous runs, cutting simulation token cost while keeping dynamics.

## Results
> "Our experiments show consistent performance trends across the evaluation approaches, while the more complex multi-hop and multi-turn setting exposes additional challenges for RAG systems." (Abstract)
> "the Conversation Cacher substantially reduces token consumption, demonstrating its potential to make dynamic evaluation more cost-efficient." (Abstract)

## Rubric
A 2 · B 2 · C 2 · D 2 · E 0 — new evaluation methodology for the Evaluation axis; six RAG configurations, compared with RAG-DIVE and CLAPNQ, industrial case; CC-BY code + data public; simulation runs with LLMs; but dynamic multi-turn user simulation is a new evaluation protocol RAG-NIMBF's static dataset adapters cannot express.

## Relevance for RAG-NIMBF
New-Techniques: dynamic multi-hop multi-turn evaluation protocol (simulated user + caching) — would need a new dataset-adapter type.

## Status log
- 2026-11-25 screened
