# 2610.38854 — Contextual Embeddings Beyond the Gold Chunk

**Score:** 8/10 · **Axis:** Embedding · [arXiv](https://arxiv.org/abs/2610.38854) · [HTML](https://arxiv.org/html/2610.38854)

## Core idea
pplx-embed-v2-context trains contextual embedding models by distilling graded chunk-level relevance from a query-aware context compression model, removing gold-chunk labels and making training targets independent of chunking. Released in 9B and 0.6B sizes with compatible embedding spaces, plus two new benchmarks (Context-bench, Q2D-Chunk) that label both answer and evidence chunks.

## Key results (verbatim quotes)
> "Our 9B model sets a new state of the art on both benchmarks and ConTEB." (Abstract)
> "Our 9B model outperforms voyage-4-large by 6.0 points and trails voyage-context-4 by 0.8 points on average" (Appendix L, BRIGHT)

## Rubric score with justification
A 2 (contextual embedding models = new Embedding axis values; multi-chunk relevance is new) · B 2 (Context-bench, Q2D-Chunk, ConTEB, ViDoRe-V3, BRIGHT) · C 1 (weights released; CC BY-NC-ND license is restrictive) · D 1 (9B needs quantisation, 0.6B fits 24 GB) · E 1 (pluggable as sentence-transformers embedding model)

## Affected axis
Embedding: The 0.6B model could be configured directly as matrix.embedding_models value (if loadable via sentence-transformers); the benchmarks are new Datasets/Evaluation material. Multi-chunk relevance labels challenge the single-gold-chunk assumption built into current eval adapters.
