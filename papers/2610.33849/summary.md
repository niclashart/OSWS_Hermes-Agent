# Ranking Is Not Deciding: Benchmark Shortcuts and Operating-Point Collapse in Query-Time RAG Poisoning Defenses (2610.33849)

**Score:** 7/10 (A:2 B:2 C:2 D:2 E:1) · **Axis:** Datasets · [arXiv](https://arxiv.org/abs/2610.33849)

## Core idea
Shows published query-time poisoning defenses score near-perfectly because poison sets share construction cues (verbatim question prefix, length cues); removing the cue collapses the decision (e.g. RAGuard AUROC 0.953 to 0.758) while ranking survives. Demands construction-profile + FPR reporting.

## Key results (verbatim quotes)
> "Deleting only that prefix from the attack authors own passages (0.93 still retrieved for their target) takes RAGuard, a published content filter we re-implement, from AUROC 0.953 to 0.758 and its miss rate from 0.191 to 0.763." (Abstract / Results)

## Rubric justification
New evaluation methodology for poisoning defenses (A=2), 4 corpora, 4 attack families, 10 defenses (B=2), code/scorer released (C=2), runs on consumer hardware (D=2), poison-set construction would be a dataset-axis concern (E=1).

## Affected axis
Datasets/Evaluation axis: poison-set construction profile and FPR-at-operating-point should become dataset registration and custom-metric fields.
