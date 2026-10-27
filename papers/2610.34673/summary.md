# Agent Memory as Recommendation: Recommender-System Design for Long-Term Memory of LLM Agents (2610.34673)

**Score:** 7/10 (A:2 B:2 C:1 D:2 E:1) · **Axis:** New-Techniques · [arXiv](https://arxiv.org/abs/2610.34673)

## Core idea
Formalizes agent memory selection as budgeted slate recommendation (request=user, memories=items, context window=slate) and proposes AgentMemRec, which adapts candidate generation, learning-to-rank and slate construction from recommenders with zero LLM calls.

## Key results (verbatim quotes)
> "On multi-session questions of LongMemEval, AgentMemRec outperforms memory and context-selection methods, including A-Mem, HippoRAG 2, DynamicRAG and T-Mem, by 10 to 31 points of accuracy." (Abstract / Results)

## Rubric justification
New memory-selection technique (A=2), LongMemEval + LoCoMo vs strong baselines (B=2), code availability unclear (C=1), no LLM calls, small models (D=2), memory layer is a new component (E=1).

## Affected axis
Not expressible: multi-session memory selection would need a new memory/context-selection axis with per-request budget; candidate new-axis proposal.
