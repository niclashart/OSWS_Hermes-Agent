# Bioformer-RetroMAE: retrieval-oriented pretraining of a compact biomedical language model for literature search (2611.19862)

Score: 8/10 (A 2, B 2, C 1, D 2, E 1)

## Core idea
43M-param biomedical embedder (RetroMAE pretraining) beats BERT-base bi-encoders.

## Key result (verbatim)
> "Compared with PubMedBERT, it improved mean average precision (MAP) by 37.0% and Recall@100 by 29.1%." (Abstract)

## Rubric justification
compact domain embedder for Embedding axis; big MAP gains vs domain baselines; C=1; 43M params trivially feasible (D=2); HF embedder value (E=1)

## Affected axis
Embedding: Embedding axis: huggingface:<id> if weights are sentence-transformers loadable; verify license at fit check.
