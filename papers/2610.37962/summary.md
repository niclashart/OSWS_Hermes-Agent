# 2610.37962 — Statistical Detection of Positional Bias in LLM-Based Recommender Systems: Methodologies and Empirical Evidence

**Score:** 7/10 · **Axis:** Evaluation · [arXiv](https://arxiv.org/abs/2610.37962) · [HTML](https://arxiv.org/html/2610.37962)

## Core idea
Two statistical methodologies (POB-ICM chi-square, POB-UNBP permutation-based uniformity null) detect positional bias in LLM-based RAG recommenders, with three metrics (permutation sensitivity, positional bias, strong positional bias). All evaluated models show structural, model-dependent bias in a controlled 40,000-instance RAG testbed.

## Key results (verbatim quotes)
> "both methodologies reject the null hypothesis of positional independence and uniformity in all evaluated state-of-the-art models" (Abstract)

## Rubric score with justification
A 2 (new evaluation methodology for prompt-order bias in RAG) · B 2 (40k instances, 20 permutations, robustness analyses) · C 2 (code publicly released) · D 2 (API-scale models, cheap permutations) · E 1 (new custom metrics for the Evaluation axis)

## Affected axis
Evaluation: Expressible as Evaluation-axis material: metrics could be added via custom_metrics_*, testbed uses a fixed prompt template — order-randomization would need a small prompt-augmentation option. Candidate for config.yaml or new-axis.md depending on the template hook.
