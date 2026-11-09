---
id: arxiv-2610.40742
title: "Prevented is Not Protected: What Attack Success Rate Hides about RAG"
authors: [et al.]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 2, D: 1, E: 1}
axis: [Evaluation]
status: rejected
screened: 2026-11-02
source: https://arxiv.org/abs/2610.40742
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.40742/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.40742/summary.md
tags: [rag-radar, Evaluation]
---
# Prevented is Not Protected: What Attack Success Rate Hides about RAG

**Axis:** [[Evaluation]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2610.40742) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.40742/paper.pdf)

## Core idea
ASR-only evaluation of RAG poisoning defenses hides defense-induced failures. "Aligned RAG Evaluation": matched-query protocol over clean/poisoned × defense on/off, with LLM-judge endorsement and retrieval-dependence controls.

## Results
> "existing defenses can introduce unexpected target-positive answers, although they can prevent some attacks, while evaluation criteria can also change defense rankings" (Abstract / Sec. 4)

## Rubric
A 2 · B 2 · C 2 · D 1 · E 1 — protocol-level evaluation change; RAG-NIMBF has no poisoning evaluation today.

## Relevance for RAG-NIMBF
Evaluation axis: would need poisoned-corpus arms + clean-utility arms + endorsement metric → `new-axis.md`.

## Status log
- 2026-11-02 screened
- 2026-11-09 fit check: rejected — security/attack evaluation framework — orthogonal to config axes, benchmark-internal interest only
