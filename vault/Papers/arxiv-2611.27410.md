---
id: arxiv-2611.27410
title: "Detecting Word-Substitution Poisoning of a RAG Knowledge Base with Relative Entropy and Runtime Verification"
authors: [Ali Yousefi, Nikos Komninos]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 0}
axis: [New-Techniques]
status: screened
screened: 2026-11-24
source: https://arxiv.org/abs/2611.27410
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.27410/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.27410/summary.md
tags: [rag-radar, New-Techniques]
---
# Detecting Word-Substitution Poisoning of a RAG Knowledge Base with Relative Entropy and Runtime Verification

**Axis:** [[New-Techniques]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.27410) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.27410/paper.pdf)

## Core idea
Detects stealth synonym-substitution poisoning of RAG corpora via relative-entropy log-ratio (AUROC 0.95), used as retrieval filter plus runtime monitor against trusted sources.

## Results
> "poisoning lowers judged answer correctness from 0.714 to 0.555" and "when it may add the trusted MITRE entry as a source, correctness rises to 0.786." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 0 — poisoning/robustness axis entirely missing in NIMBF.

## Relevance for RAG-NIMBF
Not expressible: needs new guardrail component + robustness metric. See [[New-Techniques]].

## Status log
- 2026-11-24 screened
