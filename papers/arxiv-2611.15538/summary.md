# Faithful in Steps: Improving Generalization and Citation in RAG via Query Decomposition

- arXiv/HF id: arxiv-2611.15538
- Score: 7/10 (A 2, B 2, C 1, D 1, E 1)
- Date screened: 2026-11-13
- Axis: Query-Transformation
- Source: https://arxiv.org/abs/2611.15538

## Core idea
QDRAG decomposes multi-hop (and multi-modal) questions into atomic subquestions and prunes distractor contexts with a reranker to generate faithful quotes/citations; two zero-shot decomposition modes (context-guided, retrieval-reward-guided).

## Key results (verbatim quotes)
> "The framework significantly outperforms all the baselines on both in-domain and out-of-domain tests, even surpassing Gemini-Pro." (Abstract)

## Rubric justification
A 2 · B 2 · C 1 · D 1 · E 1 — query decomposition beyond HyDE/multi-hop is not expressible; four multimodal QA benchmarks with strong baselines; finetuned MLLM, no code stated.

## RAG-NIMBF fit
Not expressible: query decomposition/rewriting other than HyDE and multi-hop follow-ups is listed as not expressible → new-axis.md candidate.
