---
id: arxiv-2611.31269
title: "Reliability of Language-Model Judges for Quantitative Scientific Question Answering: Evidence from Perovskite Photovoltaics"
authors: [Qiwei Han, Chi Zhou, Gaoxiang Yuan]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 1, E: 1}
axis: [Evaluation]
status: screened
screened: 2026-11-27
source: https://arxiv.org/abs/2611.31269
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.31269/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.31269/summary.md
tags: [rag-radar, Evaluation]
---
# Reliability of LM Judges for Quantitative Scientific QA

**Axis:** [[Evaluation]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.31269) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.31269/paper.pdf)

## Core idea
On a quantitative perovskite benchmark with deterministically computed ground truth (755 answers from 45,441 records), LLM judges agree near-perfectly with gold only when given the reference key; without it, agreement collapses (κ 0.98 → 0.56 frontier, ~0.1 local) and rankings invert, ranking a hallucinating baseline first.

## Results
> "Withholding the reference causes evaluation fidelity to collapse: frontier agreement drops to κ = 0.557 ± 0.022, and providing retrieved literature passages yields virtually no improvement (κ = 0.576 ± 0.024)." (Abstract)

> "Without reference keys, local judges degrade to near-random agreement (κ = 0.087 and 0.112), inverting the leaderboard to rank a hallucinating closed-book baseline first (τ ≤ 0.20)." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 1 · E 1 — judge-reliability protocol; 4,530 answers, 3 judges, 6 architectures; arXiv non-exclusive license; needs frontier judge; reference-keyed judging not a config value.

## Relevance for RAG-NIMBF
Argues for deterministic reference answers + exact-match-style metrics over LLM judges on quantitative datasets (`dataset_ground_truth_field`, custom metrics). Judge-agreement measurement (κ vs. gold, judge-swap sensitivity) would be a new evaluation mode.

## Status log
- 2026-11-27 screened
