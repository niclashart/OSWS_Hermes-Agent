# RAG-Stress: Probing the Limits of Evidence Reliance in Retrieval-Augmented Generation

**Axis:** [[Evaluation]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2610.11183) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/2610.11183/paper.pdf)

## Core idea
Controlled diagnostic protocol for evidence reliance: holds question fixed, edits one evidence assertion to support a wrong answer, and measures misleading rate (MR) — how often models replace a correct closed-book answer after retrieval.

## Results
> "Instructions that prioritize documents consistently produce higher MR than those permitting reliance on prior knowledge. Averaged over models and positions, the gap ranges from 10.9 to 13.5 percentage points across the three QA datasets." (Sec. 4.3)
> "Mean MR follows End > Beginning > Middle under both policies" (Sec. 4.3)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — new evaluation protocol (misleading rate) for the Evaluation axis; 15 systems, 3+ datasets, paired audits; no code release stated; runs with open/API models; protocol needs new metric + evidence-editing component.

## Relevance for RAG-NIMBF
MR could be added as a `custom_metrics_*` diagnostic; the controlled evidence-editing harness is a new component.

## Status log
- 2026-10-24 screened
