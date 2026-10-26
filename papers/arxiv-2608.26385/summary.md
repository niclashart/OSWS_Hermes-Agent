# Why RAGs Hallucinate: Penalty-Aware Evaluation with Knowledge-Gap Canaries

**arXiv:** https://arxiv.org/abs/2608.26385 · **Score:** 8/10 (A2 B2 C2 D2 E1) · **Axis:** Evaluation · **Screened:** 2026-10-26

## Core idea
Penalty-aware RAG evaluation (asymmetric scoring + knowledge-gap canaries + failure attribution) reorders volume-based rankings; canary violation rates differ sixfold across systems.

## Key results (verbatim quotes)
- "canary violation rates differ roughly sixfold (16.7% vs. 98.1%)" (Abstract)
- "The systems are separated less by what they answer correctly than by whether they answer at all when they should not" (Abstract)

## Rubric justification
- A=2: knowledge-gap canaries + penalty-aware scoring = new Evaluation/Datasets option
- B=2: SimpleQA-Verified, 98.9% judge unanimity, sixfold canary-rate separation, stable reordering k=1..9
- C=2: code and judge votes released for audit
- D=2: evaluation-only
- E=1: needs new custom metric + canary dataset support

## RAG-NIMBF fit
Custom metrics exist in RAG-NIMBF but canary questions and asymmetric scoring need new settings; candidate new-axis.
