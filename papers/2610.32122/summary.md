# Semantically Rich, Metrically Affect-Blind: A Geometric Blind Spot in Modern Text Embedders (2610.32122)

**Score:** 7/10 (A:2 B:2 C:2 D:2 E:1) · **Axis:** Embedding · [arXiv](https://arxiv.org/abs/2610.32122)

## Core idea
Shows sentiment is linearly decodable from modern embedder outputs (up to 91.3%) yet nearly absent from their cosine metric; a small supervised-contrastive injection head (0.13M-0.69M params, CPU-trained) recovers MAP for affect tasks at a cost on STS.

## Key results (verbatim quotes)
> "The head improves every encoder released since 2022 on full-data probe accuracy (up to +5.8 points), retrieval MAP (up to +26.0) and polarity margin (7-61x)." (Abstract / Results)

## Rubric justification
Embedder metric property relevant to Embedding axis (A=2), 11 encoders, controls and ablations (B=2), code public (C=2), CPU-training of head, small encoders (D=2), would need injection-head support in the embedding slot (E=1).

## Affected axis
Embedding axis evidence: default retrieval embeddings are blind to affect; an injected-head embedding variant would need a new `embedding_models` wrapper/adapter.
