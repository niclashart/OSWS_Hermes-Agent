# Re$^3$Rank: Listwise Reranking with Reasoning-Conditioned Retrieval Heads

- arXiv: https://arxiv.org/abs/2611.02550
- Screened: 2026-11-04 · Score: 9/10 · Rubric A-E: (2, 2, 2, 2, 1)
- Axis: Reranking

## Core idea
Listwise reranker where a generator writes a reasoning trace and a scorer reads relevance from retrieval-head attention using the trace as query; joint training via straight-through estimator; 4B beats strongest baseline by 3.11 NDCG@10, 0.6B beats 32B rerankers.

## Key results (verbatim quotes)
> "our 4B variant exceeds the strongest baseline by 3.11 NDCG@10 points on average, and even our 0.6B variant surpasses rerankers with up to 32B parameters." (Abstract)

## Rubric justification
A=2: reasoning-conditioned listwise reranking; B=2 nine benchmarks, 11 baselines; C=2 code + HF model weights; D=2 0.6B-4B models; E=1 LLM listwise reranker = new provider (not sentence-transformers CrossEncoder).

## RAG-NIMBF relevance
Maps to the **Reranking** axis; see vault note.
