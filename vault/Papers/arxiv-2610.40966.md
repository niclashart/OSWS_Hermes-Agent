---
id: arxiv-2610.40966
title: "Better Retrievers, Worse Labels: How Incomplete Relevance Judgments Distort Abstention Evaluation in Conversational RAG"
authors: [et al.]
year: 2026
score: 9
rubric: {A: 2, B: 2, C: 2, D: 2, E: 1}
axis: [Evaluation]
status: fit
screened: 2026-11-02
source: https://arxiv.org/abs/2610.40966
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.40966/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.40966/summary.md
tags: [rag-radar, Evaluation]
---
# Better Retrievers, Worse Labels: How Incomplete Relevance Judgments Distort Abstention Evaluation in Conversational RAG

**Axis:** [[Evaluation]] · **Score:** 9/10 · [arXiv](https://arxiv.org/abs/2610.40966) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2610.40966/paper.pdf)

## Core idea
Scoring abstention by gold-document presence breaks as retrievers improve: no-gold contexts increasingly still contain the answer, so refusal precision collapses and answerability AUROC is far too low.

## Results
> "The stronger the retriever, the larger the share of no-gold contexts that still contain the answer (28% to 72%) and the lower the shortcut's precision (.68 to .10)" (Abstract)
> "answerability AUROC is up to .19 too low" (Sec. 4)

## Rubric
A 2 · B 2 · C 2 · D 2 · E 1 — evaluation-protocol finding; needs content-based sufficiency labels, not a single config value.

## Relevance for RAG-NIMBF
Evaluation axis: refusal/abstention metrics must use content sufficiency labels, not gold-presence. Likely `new-axis.md` (new metric/label mode).

## Status log
- 2026-11-02 screened
- 2026-11-02 fit-check (W45): not expressible (abstention labels need content sufficiency, not gold-doc presence) → proposals/arxiv-2610.40966/new-axis.md; status fit
- 2026-11-11 impl-check: see implementations/2026-W46/arxiv-2610.40966.md
