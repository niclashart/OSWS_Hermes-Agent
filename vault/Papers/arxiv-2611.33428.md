---
id: arxiv-2611.33428
title: "When the Knowledge Runs Out: A Part-Level Pilot Evaluation of How Language Models Handle Partially Covered Questions"
authors: [Vahid Mohammadi]
year: 2026
score: 8
rubric: {A: 2, B: 1, C: 2, D: 2, E: 1}
axis: [Evaluation, Prompting]
status: screened
screened: 2026-11-27
source: https://arxiv.org/abs/2611.33428
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.33428/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.33428/summary.md
tags: [rag-radar, Evaluation]
---
# When the Knowledge Runs Out

**Axis:** [[Evaluation]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.33428) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.33428/paper.pdf)

## Core idea
Part-level evaluation of multi-part questions with partially covering reference material. Six per-part verdicts separate gap-filling (unsupported_claim) from the subtler answer_plus_claim failure. Shows an abstain instruction nearly eliminates gap-filling, and that RAGAS faithfulness penalises correct withholding.

## Results
> "Without an explicit instruction to stay within the material, both models fill most gaps from their own knowledge (unsupported-claim rates of 0.71 and 0.90). One added sentence instructing them to answer only from the material brings these rates to 0.00 and 0.06" (Abstract)

> "boundary_accuracy .54 → .99 (claude-haiku-4-5), .44 → .87 (llama3.1:8b)" (Table 2, Sec. 4)

## Rubric
A 2 · B 1 · C 2 · D 2 · E 1 — new Evaluation protocol; small 30-case pilot; open dataset+code CC BY; runs on llama3.1:8b via Ollama; per-part judge metrics need new custom metric.

## Relevance for RAG-NIMBF
Grounded vs. default condition = existing `abstain_strict` vs. default prompt. Per-part verdict metrics (unsupported-claim rate, boundary accuracy) are new custom metrics beyond RAGAS faithfulness.

## Status log
- 2026-11-27 screened
