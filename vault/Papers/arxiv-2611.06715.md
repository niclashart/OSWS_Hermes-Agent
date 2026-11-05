---
id: arxiv-2611.06715
title: "Reasoning over Non-Parametric Memory in Multilingual LLMs: A Cognitive-Based Analysis of Relational Knowledge"
authors: [Zohreh Abbasi Liasi, Batoul Ham, ...]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 2, D: 2, E: 0}
axis: [Datasets, Evaluation]
status: screened
screened: 2026-11-05
source: https://arxiv.org/abs/2611.06715
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.06715/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.06715/summary.md
tags: [rag-radar, Datasets]
---
# Rel-Bloom (Evidence-Conditioned Relational Reasoning)

**Axis:** [[Datasets]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.06715) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.06715/paper.pdf)

## Core idea
Rel-Bloom: 450 multilingual MCQs from 30 Wikidata relations at five Bloom levels and three veracity conditions, facts given directly in the prompt (no retriever). Diagnoses whether generators reason over supplied RAG context vs memorized associations — the assumption RAG evaluation rests on.

## Results
> "accuracy drops sharply from Apply to Analyze in every evaluated open-weight model series, reaching 47.2 percentage points for the Large Granite bucket" (Abstract / Sec. 4.2)
> "Gemini 3.1 Pro averages 99.5% on the other four levels but 60.7% on Evaluate" (Abstract)

## Rubric
A 2 · B 2 · C 2 · D 2 · E 0 — new evaluation benchmark; 43 models/6 languages/statistics; resources public; consumer-GPU MCQ; needs new dataset adapter (Bloom/veracity metadata).

## Relevance for RAG-NIMBF
Candidate `hf-generic`-style dataset adapter with cognitive-level and veracity fields; enables generator-faithfulness axes beyond RAGAS.

## Status log
- 2026-11-05 screened
