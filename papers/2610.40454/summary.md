# 2610.40454 — Glance: The Generator Is Its Own Reranker

**Score:** 8/10 · **Axis:** Reranking · [arXiv](https://arxiv.org/abs/2610.40454) · [HTML](https://arxiv.org/html/2610.40454)

## Core idea
Glance turns the RAG generator itself into the reranker: after a single shared prefill of all k candidate passages, short relevance probes branch from the cached context and a 256-dim pointer head converts each probe into a relevance score, removing the separate cross-encoder model and per-pair prefilling. A 9B backbone serves generation, decisions and reranking with ~0.1 GiB extra per decision skill.

## Key results (verbatim quotes)
> "After 39 minutes of MS MARCO fine-tuning, Glance achieves nDCG@10 of 0.741 on SciFact and 0.345 on NFCorpus, compared with 0.721 and 0.326 for bge-reranker-v2-m3." (Abstract)

## Rubric score with justification
A 2 (fuses reranking into generator, new axis needed) · B 2 (BEIR + HotpotQA + scaling study vs strong cross-encoder) · C 2 (adapters + code on HF, CC BY 4.0) · D 2 (9B, runs on 24 GB) · E 1 (needs adapter/pointer-head component, not a config value)

## Affected axis
Reranking: Not expressible today: reranking happens inside the generator backbone, not via matrix.reranker_models. Needs a new RAG-System/Generator-level option 'generator-reranking' or a new-axis proposal. A 0.6B-style variant could later serve as a custom reranker value.
