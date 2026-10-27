# System One models Are Not Better Rerankers (2610.32318)

**Score:** 8/10 (A:2 B:2 C:2 D:2 E:2) · **Axis:** Reranking · [arXiv](https://arxiv.org/abs/2610.32318)

## Core idea
Compares decision fine-tuned (System One) models against reranker fine-tunes of the same Qwen backbones (0.6B-27B) on 10 TREC DL/BEIR collections: decision fine-tuning never wins; reranker fine-tuning wins by 5-29 nDCG@10 up to 9B, tie at 27B.

## Key results (verbatim quotes)
> "From 0.6B to 9B, reranker fine-tuning wins on every backbone by 5 to 29 points nDCG@10, also on zero-shot collections, and at 27B the two tie." (Abstract / Results)

## Rubric justification
Direct evidence for the Reranking axis (A=2), 6 backbones x 10 collections (B=2), training code released (C=2), 0.6B-9B models feasible (D=2), maps to existing reranker_models slot (E=2).

## Affected axis
Directly informs `matrix.reranker_models` value choice: prefer reranker fine-tunes (e.g. castorini-style) over decision-model checkpoints at <= 9B.
