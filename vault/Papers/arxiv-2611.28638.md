---
id: arxiv-2611.28638
title: "Make Position Uninformative: Exchangeable Self-Distillation Flattens the Lost-in-the-Middle Curve"
authors: [Qingsen Ma, Dianyun Wang, Jiahong Liu, Irwin King]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-11-24
source: https://arxiv.org/abs/2611.28638
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.28638/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.28638/summary.md
tags: [rag-radar, New-Techniques]
---
# Make Position Uninformative: Exchangeable Self-Distillation Flattens the Lost-in-the-Middle Curve

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.28638) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.28638/paper.pdf)

## Core idea
ExSD trains a small LoRA adapter on shuffled contexts to reproduce the model's answer when reading the answer document alone — no gold answers, ~2.3k examples — removing the lost-in-the-middle U-curve.

## Results
> "On six models from 1.5B to 32B parameters, ExSD raises both average and worst-position accuracy against the frozen model, including on a held-out test split." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 0 — needs a training loop; NIMBF has no trained-generator support.

## Relevance for RAG-NIMBF
Not expressible: trained reader adapters unsupported; relevant to the long-context vs RAG gap.

## Status log
- 2026-11-24 screened
