# dotproductx/breadbowl-embed-v1.3 (HF model, embedder)

## Core idea
Late-interaction slot model on a Qwen3.5-0.8B backbone: each passage is encoded once into 16 slots, each holding a 256-d routing vector (candidate finding) and a 256-d value vector (reranking by attention over stored values — no model pass at query time). Score = 0.75 × routing + 0.25 × value.

## Key results (model card, self-reported)
> "Level with Qwen3-Embedding-0.6B + Qwen3-Reranker-0.6B on MS MARCO and DL19, and 5.5 nDCG@10 ahead on DL20."

> "50× faster rerank. 2.9 ms against 150 ms on the same candidates." (one RTX 5090; cross-encoder Qwen3-Reranker-0.6B)

> "BEIR: 55.1 mean over 15 tasks, 3.6 above v1.2-preview."

MS MARCO dev nDCG@10 41.71 (QKV), Recall@100 84.46; DL19 74.63; DL20 headline numbers in card. License: Apache-2.0 weights, code at github.com/BreadBowlAI/breadbowl-embed (library `breadbowl-embed`, not sentence-transformers). Limits: ~70 ms/query on CPU, CUDA not yet validated in the library; load with dtype bfloat16.

## Rubric score: 8/10
A 2 — beats the Qwen3-Embedding-0.6B + Qwen3-Reranker-0.6B stack users run (level/above on 3 datasets), replaces two models with one. B 2 — full 8.8M-passage corpora, BEIR 15 tasks, baselines named. C 2 — Apache-2.0 weights + code. D 1 — 0.8B backbone fits consumer GPUs, but CUDA path unvalidated in the library. E 1 — late-interaction slot model: not loadable via sentence-transformers `SentenceTransformer`/`CrossEncoder`, so no direct `huggingface:` slot; new provider needed (per rubric, late interaction = E 1).

## Affected axis
Embedding + Reranking (combined single-model retriever+reranker; New-Techniques for the slot/routing index).

## Ready-to-use slot line
Not slot-ready: needs a new provider (custom index over routing/value vectors), not `embedding_models`/`reranker_models`.
