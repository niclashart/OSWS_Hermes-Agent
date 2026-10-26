# Debiasing as a Measurement Intervention: Calibrated Ties and Resolution Loss in LLM-as-a-Judge Evaluation

**arXiv:** https://arxiv.org/abs/2609.12439 · **Score:** 7/10 (A2 B2 C2 D2 E0) · **Axis:** Evaluation · **Screened:** 2026-10-26

## Core idea
TraceJudgeBench shows anti-citation debiasing prompts can destroy judge resolution (validated gaps become Ties); debiasing must be reported jointly with resolution retention.

## Key results (verbatim quotes)
- "stronger anti-citation prompts reduce worse-cited wins from up to 50.5% to 0%; yet some operating points already convert validated moderate-gap decisions into Tie" (Abstract)
- "TRACE-style decoupling recovers 96.5-100.0% better-plain resolution across the reported settings." (Abstract)

## Rubric justification
- A=2: TraceJudgeBench is a new diagnostic dataset for Evaluation axis
- B=2: across three frontier + two open-weight judges, human-validated gaps, second FinQA construction
- C=2: supplementary artifact released
- D=2: Qwen2.5-14B-AWQ and Gemma-3-12B reproduce the frontier
- E=0: concerns eval protocol, not pipeline config

## RAG-NIMBF fit
Useful as Evaluation-axis dataset; adding it would need a new registered dataset adapter.
