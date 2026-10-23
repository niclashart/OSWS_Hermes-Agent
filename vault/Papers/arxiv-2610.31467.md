---
id: arxiv-2610.31467
title: "From Structured Records to Patient Narratives: Preserving Clinical Alignment in LLM-Generated Health Summaries"
authors: [Bayram Ayadi]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 2, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-10-23
source: https://arxiv.org/abs/2610.31467
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.31467/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.31467/summary.md
tags: [rag-radar, New-Techniques]
---
# From Structured Records to Patient Narratives: Preserving Clinical Alignment in LLM-Generated Health Summaries

**Axis:** [[New-Techniques]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2610.31467) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.31467/paper.pdf)

## Core idea
Constrained-generation framework combining structured evidence conditioning with RAG for patient-facing health summaries; evaluated with NLI, atomic factuality and readability across three LLMs and 4,500 summaries.

## Results
> "explicit grounding constraints consistently improve clinical alignment, particularly by improving uncertainty preservation and, once faithfulness is evaluated against retrieved evidence, generally preserving or improving faithfulness, while effects on omission remain model-dependent" (Abstract)

## Rubric
A: 2, B: 2, C: 1, D: 2, E: 0 — grounding-constraint prompting with faithfulness-vs-evidence evaluation; no public code found

## Relevance for RAG-NIMBF
Not expressible: prompt-based constrained generation stage between retrieval and answering has no NIMBF config key. Candidate for new-axis.md in weekly fit check.

## Status log
- 2026-10-23 screened
