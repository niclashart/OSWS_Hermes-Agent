---
id: hf-nvidia_Nemotron-3.5-Rerank-1B-BF16
title: "nvidia/Nemotron-3.5-Rerank-1B-BF16"
authors: [NVIDIA]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [Reranking]
status: screened
screened: 2026-11-28
source: https://huggingface.co/nvidia/Nemotron-3.5-Rerank-1B-BF16
pdf: 
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-nvidia_Nemotron-3.5-Rerank-1B-BF16/summary.md
tags: [rag-radar, Reranking]
---
# nvidia/Nemotron-3.5-Rerank-1B-BF16

**Axis:** [[Reranking]] · **Score:** 8/10 · [HF](https://huggingface.co/nvidia/Nemotron-3.5-Rerank-1B-BF16) · [Summary](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-nvidia_Nemotron-3.5-Rerank-1B-BF16/summary.md)

## Core idea
1.6B multilingual (34 languages incl. German) + multimodal (text / page image / both) cross-encoder reranker from NVIDIA; slot line `reranker_models: huggingface:nvidia/Nemotron-3.5-Rerank-1B-BF16`.

## Results
> "Benchmark Score: NDCG@10" — ViDoRe V3 63.50 (image) / 64.66 (text) / 64.79 (image+text), MIRACL-VISION 72.17; beats Qwen3-VL-Reranker-2B on all four (+2.6 to +6.9). (model card, Evaluation Dataset)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — beats Qwen3-VL-Reranker-2B on public benchmarks; OpenMDW-1.1 license; multimodal reranking = new provider (E 1), text reranking slot-ready.

## Relevance for RAG-NIMBF
Text reranking: `huggingface:` CrossEncoder slot. Multimodal/page-image reranking: not expressible today (new-axis candidate).

## Status log
- 2026-11-28 screened (HF model: no PDF, mteb link absent)
