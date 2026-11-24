---
id: arxiv-2611.27350
title: "GRACE: Controlled Evidence Interventions for Diagnosing and Improving Knowledge Integration in GraphRAG"
authors: [Minh Pham, Quang Nguyen]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 1, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-11-24
source: https://arxiv.org/abs/2611.27350
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.27350/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.27350/summary.md
tags: [rag-radar, New-Techniques]
---
# GRACE: Controlled Evidence Interventions for Diagnosing and Improving Knowledge Integration in GraphRAG

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.27350) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.27350/paper.pdf)

## Core idea
GraphRAG benchmark with four controlled evidence interventions (severed support path, distractors, hubs, counterfactual answer) over Wikidata; plus QCFSE-SA model with a calibrated graph-support gate.

## Results
> "it improves controlled-state accuracy from 57.17% to 62.78% (+5.61 points; question-clustered 95% CI [+5.04, +6.17]) and broken-state accuracy from 55.41% to 67.85%." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 1 · E 0 — controlled evidence-state evaluation is a strong Evaluation-axis candidate; graph retrieval unsupported in NIMBF.

## Relevance for RAG-NIMBF
Not expressible: no knowledge-graph retrieval, no evidence-intervention evaluation harness. See [[New-Techniques]].

## Status log
- 2026-11-24 screened
