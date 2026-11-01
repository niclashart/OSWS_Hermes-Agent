---
id: hf-nlpai-lab_KURE-v3
title: "nlpai-lab/KURE-v3"
authors: [nlpai-lab]
year: 2026
score: 9
rubric: {A: 1, B: 2, C: 2, D: 2, E: 2}
axis: [Embedding]
status: screened
screened: 2026-11-01
source: https://huggingface.co/nlpai-lab/KURE-v3
pdf: 
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-nlpai-lab_KURE-v3/summary.md
tags: [rag-radar, Embedding]
---
# nlpai-lab/KURE-v3

**Axis:** [[Embedding]] · **Score:** 9/10 · [HF](https://huggingface.co/nlpai-lab/KURE-v3) · [Summary](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-nlpai-lab_KURE-v3/summary.md)

## Core idea
Korean–English bilingual dense retriever, 1.1B params (Nemotron-3-Embed-1B base), 2048-d Matryoshka vectors (256–2048 truncatable), 8,192-token context, 0.8027 nDCG@10 on MTEB(kor, v2) Retrieval — above 8B models.

## Results
> "With 1.1B parameters, it averages **0.8027** nDCG@10 on MTEB(kor, v2) Retrieval. It outperforms 8B dense models such as comsat-embed-ko-8b-preview and Qwen3-Embedding-8B." (model card)

## Rubric
A 1 · B 2 · C 2 · D 2 · E 2 — Korean-specific (A max 1 per rubric), but public MTEB leaderboard numbers with baselines, apache-2.0, plain `SentenceTransformer`.

## Relevance for RAG-NIMBF
Expressible (E=2): `embedding_models: huggingface:nlpai-lab/KURE-v3`. Would need a Korean dataset for a meaningful proposal; not useful for the current German/English default setup.

## Status log
- 2026-11-01 screened (HF model: no PDF, mteb link present)
