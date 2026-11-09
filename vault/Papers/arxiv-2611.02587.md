---
id: arxiv-2611.02587
title: "They Know Where It Is, But Not What It Says: A Bilingual Hallucination Benchmark of Hadith Recall in Open LLMs"
authors: [et al.]
year: 2026
score: 8
rubric: {A: 1, B: 2, C: 2, D: 2, E: 1}
axis: [Evaluation]
status: rejected
screened: 2026-11-04
source: https://arxiv.org/abs/2611.02587
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.02587/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.02587/summary.md
tags: [rag-radar, Evaluation]
---
# They Know Where It Is, But Not What It Says: A Bilingual Hallucination Benchmark of Hadith Recall in Open LLMs

**Axis:** [[Evaluation]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.02587) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.02587/paper.pdf)

## Core idea
Bilingual benchmark (EN/AR) probing five open-weight LLMs on exact Hadith recall without retrieval: no model reproduces the source text exactly; authors argue verified-corpus RAG should be mandatory for such high-stakes recall.

## Results
> "0% of 30,000 responses achieve both high lexical and high semantic fidelity, i.e., an exact, verifiable match to the source text."…

## Rubric
A 1 · B 2 · C 2 · D 2 · E 1 — direct-mode (no-retrieval) hallucination evaluation, supports the retrieval_mode: direct baseline (Evaluation); B=2 30k scored responses; C=2 code public; D=2 s

## Relevance for RAG-NIMBF
Candidate for the **Evaluation** axis at the weekly fit check.

## Status log
- 2026-11-04 screened
- 2026-11-09 fit check: rejected — Hadith recall benchmark — domain benchmark, not RAG-pipeline relevant
