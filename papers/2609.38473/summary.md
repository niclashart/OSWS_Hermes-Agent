# Re-ranking and Late Interaction Drive Retrieval Quality: A Controlled Comparison of RAG Strategies for Scientific Question Answering (2609.38473)

**Score: 10/10** · [arXiv](https://arxiv.org/abs/2609.38473) · screened 2026-10-25

## Core idea
Controlled comparison of six RAG retrieval strategies (dense top-k, query rephrasing, LLM reranking, RRF fusion, agentic tool-call retrieval, ColBERTv2 late interaction) on 464k arXiv papers with a shared generator and judge protocol; open code + 19,484 synthetic questions.

## Key results
> "All six pipelines share the same generator (Meta-Llama/Llama-3.1-8B-Instruct), prompt, and evaluation protocol; the five single-vector pipelines additionally share SPECTER2 embeddings and a Chroma vector store; and all six retrieve from the full corpus of 463,971 arXiv papers dated 2024-2025." (Abstract)

## Rubric
A 2 · B 2 · C 2 · D 2 · E 2 = 10 — A2 · B2 · C2 · D2 · E2 — controlled multi-strategy comparison on a large corpus, CC BY 4.0 code+data, Llama-3.1-8B on consumer hardware; reranking/RRF map to existing NIMBF axes.

## Affected axis
Reranking

## Relevance for RAG-NIMBF
Direct grid experiment: reranker values (`matrix.reranker_models`) vs RRF-style query transformation vs baseline `similarity`. RRF fusion itself and the agentic tool-call strategy are not expressible today (→ weekly fit check).
