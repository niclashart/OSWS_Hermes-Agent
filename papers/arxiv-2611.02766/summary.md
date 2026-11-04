# EffComp: Efficient Prompt Compression via Hybrid Reinforcement & Supervised Learning

- arXiv: https://arxiv.org/abs/2611.02766
- Screened: 2026-11-04 · Score: 8/10 · Rubric A-E: (2, 2, 1, 2, 1)
- Axis: New-Techniques

## Core idea
Extractive prompt compression for RAG QA: a BERT-style reranker and sentence selector, trained with hybrid RL + supervised learning, cut context to a compression ratio while preserving LLM accuracy with minimal latency; extractive, so no hallucination risk.

## Key results (verbatim quotes)
> "EffComp outperforms state-of-the-art prompt compression methods achieving the best trade-off between compression ratio and accuracy with minimal latency." (Abstract)

## Rubric justification
A=2: context compression under a token budget — explicitly not expressible today; B=2 multiple QA datasets vs SOTA; C=1 no code mentioned; D=2 BERT-size models; E=1 new post-retrieval pipeline component.

## RAG-NIMBF relevance
Not expressible as a single config value — new technique (see New-Techniques / New-Techniques).
