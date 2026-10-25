# AGO AI Quality Gate: Evidence-First Release Decisions for Retrieval-Augmented Generation (2610.01218)

**Score: 7/10** · [arXiv](https://arxiv.org/abs/2610.01218) · screened 2026-10-25

## Core idea
Evidence-first quality-gate framework for RAG release decisions: four-state decision model, layered scoring, beta-binomial regression-risk gate, and mandatory LLM-judge meta-evaluation before the judge influences decisions.

## Key results
> "a low-cost judge (gpt-4.1-nano) detects non-adherent answers barely above chance (AUROC 0.603 [0.570, 0.634]), despite producing flawless protocol output, while gpt-4o reaches 0.783 [0.756, 0.807] -- yet its per-domain performance still ranges from 0.62 to 0.88." (Abstract (judge layer evaluated on RAGBench))

## Rubric
A 1 · B 2 · C 1 · D 2 · E 1 = 7 — A1 · B2 · C1 · D2 · E1 — RAGBench (100k traces, 12 datasets) evaluation; engagement framework part is proprietary; contributes judge-validation methodology to the Evaluation axis.

## Affected axis
Evaluation

## Relevance for RAG-NIMBF
Judge meta-evaluation could inform `settings.eval_critic_*` usage (validate critic before comparing configs); gate machinery itself is not a pipeline axis.
