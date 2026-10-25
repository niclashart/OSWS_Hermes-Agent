# Relevance Is Not Sufficient Evidence: Detecting Evidence Gaps Before Generation in RAG (2609.37469)

**Score: 8/10** · [arXiv](https://arxiv.org/abs/2609.37469) · screened 2026-10-25

## Core idea
RINSE: a pre-generation gate that judges from question+retrieved passages alone whether the evidence is sufficient, combining question-coverage, answer-span evidence, and a small local LLM reader. Skips generation when evidence is insufficient.

## Key results
> "Across six datasets, RINSE ranks sufficient above insufficient evidence with a score of 0.837 (chance 0.5), exceeding the best of 10 prior methods (0.746) and a frontier model queried through an API (0.784). RINSE runs locally before generation, taking 36.5 ms per question on a single GPU." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 = 8 — A2 · B2 · C1 · D2 · E1 — six datasets with leakage-controlled contrast construction; code release unclear; small local model; needs a new pre-generation component.

## Affected axis
New-Techniques

## Relevance for RAG-NIMBF
Not expressible: RAG-NIMBF has no sufficiency-gate component before generation. Candidate for `new-axis.md` (retrieval_mode extension or new gate component).
