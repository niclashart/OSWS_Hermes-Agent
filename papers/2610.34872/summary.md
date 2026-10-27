# Adaptive Retrieval, Selective Answers: Evaluating Conformal Factuality in Agentic RAG (2610.34872)

**Score:** 7/10 (A:2 B:2 C:2 D:2 E:1) · **Axis:** Evaluation · [arXiv](https://arxiv.org/abs/2610.34872)

## Core idea
Applies claim-level conformal factuality filtering after agentic RAG (adaptive follow-up retrieval + termination) and characterizes the reliability-informativeness trade-off: stricter conformal targets raise full-support rates but drastically cut answer availability.

## Key results (verbatim quotes)
> "At the 95% target, non-empty response coverage ranges from 17.23% to 60.17%, claim retention from 10.72% to 43.16%, and full support among non-empty outputs from 89.14% to 95.56%." (Abstract / Results)

## Rubric justification
New evaluation protocol for agentic RAG (A=2), 6 configurations x 100 seeded partitions (B=2), code public (C=2), GPT/Llama 8B feasible (D=2), conformal filtering would be a new post-generation component (E=1).

## Affected axis
Evaluation axis material: a conformal-factuality custom metric could extend `settings.custom_metrics_*`, but the agentic retrieval loop it evaluates is not expressible.
