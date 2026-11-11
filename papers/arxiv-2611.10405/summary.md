# Yuanbao-Reranker: Document-Grounded Synthesis and Preference Distillation for Text Reranking

arXiv 2611.10405 · Tencent Yuanbao Search · model family 0.6B / 4B / 8B on Qwen3 backbone (HuggingFace: tencent/Yuanbao-Reranker-{0.6B,4B,8B})

## Core idea
Dense pointwise reranker family trained on 2.75M 1:3 ranking groups from document-grounded query synthesis with a three-stage curation funnel (positive support verification, dedup, quotas), false-negative filtering by teacher score margin, and tiered negatives; joint pointwise CE + bounded minimum-gap hinge objective with cross-scale distillation and layerwise model merging.

## Key results (verbatim)
> "the 0.6B variant reaches 70.96 Avg. to surpass 1B–4B active-parameter baselines, the 4B variant reaches 73.63 Avg. to outperform the 8B teacher (72.68), and the 8B variant achieves a state-of-the-art 74.21 Avg." (Abstract; benchmarks CMTEB-R, MMTEB-R, BEIR, MLDR, MTEB-Code)

> "adding curated synthetic data raises the five-panel average from 68.77 to 70.43 ( +1.66 )" (§5.1, Table 2)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 2 — 9/10 → relevant. Beats the bge-reranker/Qwen3-Reranker class across 5 panels at every size; 0.6B runs easily on consumer GPU. License of released weights to confirm on HF (C=1 pending); loadable as sentence-transformers CrossEncoder → direct `reranker_models` config value.

## Affected axis
Reranking — candidate config value `reranker_models: huggingface:tencent/Yuanbao-Reranker-0.6B` (sentence-transformers CrossEncoder compatible; verify on the HF card before the weekly fit check).

## Status log
- 2026-11-11 screened
