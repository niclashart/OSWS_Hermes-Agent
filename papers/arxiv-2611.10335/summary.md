# Two-Sided Conformal Evidence Sets for Retrieval-Augmented Generation

arXiv 2611.10335

## Core idea
Conformal Evidence Sets (CES): returns separate *support* and *refutation* passage sets with finite-sample coverage ≥ 1−α per side (Bonferroni joint ≥ 1−2α) under exchangeability — calibrated grounding beyond one-sided support-only methods.

## Key results (verbatim)
> "On labeled candidate pools from the contrastive VitaminC benchmark, CES closely tracks nominal coverage across α∈{0.05,0.10,0.15,0.20,0.30}, with maximum deviations of 3.0 percentage points for support and 5.4 for refutation" (Abstract)

> "under FEVER distribution shift both sides under-cover, by up to 12.7 percentage points" (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 1 · E 1 — 7/10 → relevant. New evaluation/guardrail technique (calibrated evidence coverage as a reportable metric distinct from verdict accuracy); coverage experiments with stress tests; no public code found (C=1); exchangeability-based recalibration is a post-retrieval component, new adapter needed (E=1).

## Affected axis
Evaluation / New-Techniques — coverage guarantees for evidence sets are not expressible in RAG-NIMBF today.

## Status log
- 2026-11-11 screened
