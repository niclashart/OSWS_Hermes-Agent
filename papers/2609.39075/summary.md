# RAGScope: A Leakage-Controlled, Cost-Aware Evidence-Gating Protocol for RAG Hallucination Triage (2609.39075)

**Score: 8/10** · [arXiv](https://arxiv.org/abs/2609.39075) · screened 2026-10-25

## Core idea
Leakage-controlled evaluation protocol plus a cheap CPU evidence gate (RAGScope-E) that routes RAG answers: accept low-risk, review uncertain. 6.22 ms/example on CPU vs 145–223 ms for NLI/HHEM verifiers.

## Key results
> "At a top-10% review budget, RAGScope-E attains 0.748 precision; accepting the lowest-risk 50% yields 0.141 residual unfaithfulness. RAGScope-E runs in 6.22 ms/example on CPU, versus 145.75 and 223.07 ms/example for the tested DeBERTa-NLI and HHEM settings." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 = 8 — A2 · B2 · C1 · D2 · E1 — RAGTruth + HaluBench stress test with source-shift analysis; gate is an answer-routing component.

## Affected axis
New-Techniques

## Relevance for RAG-NIMBF
Post-generation evidence gating is not expressible today → `new-axis.md` (Evaluation or new gate component).
