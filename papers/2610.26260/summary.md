# Preference Is Not Position: Evaluating Reranking on NevIR in Fixed Hybrid Candidate Pools (arXiv:2610.26260)

## Core idea
Distinguishes pairwise preference (ordering a near-identical pair, e.g. negation) from position (preferred passage early in the list). Evaluates rerankers on NevIR pairs inside fixed hybrid candidate pools (dense, learned sparse, BM25) with both metrics plus cost.

## Results
> "Qwen3-14B-AWQ with fusion tie-breaking reaches 77.45% strict preference, 58.99% NevIR-style paired accuracy across 1,363 complete pairs, and preferred-passage MRR of 0.7509. A BGE cross-encoder reaches 69.77% strict preference and MRR of 0.7404" (Abstract). Pairwise-trained ranker improves preference (56.62% vs 52.30%) but cuts MRR from 0.5764 to 0.3055.

## Rubric
A 2 · B 2 · C 2 · D 2 · E 1 — reranking evaluation protocol on negation-sensitive pairs; Qwen/BGE rerankers are pluggable as `sentence-transformers/<hf-id>` values or LLM judge.

## Relevance for RAG-NIMBF
Reranking axis: add LLM-as-reranker (Qwen3-14B-AWQ) vs BGE cross-encoder comparison; joint preference+position metrics for Evaluation axis.
