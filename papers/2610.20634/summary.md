# Jev-as-a-Judge for RAG Claim Verification: Confidence-Gated Cascading Between a Non-Generative Verifier and a Frontier LLM (2610.20634)

**Score: 7/10** · [arXiv](https://arxiv.org/abs/2610.20634) · screened 2026-10-25

## Core idea
Confidence-gated cascade for claim verification: a cheap non-generative verifier handles confident claims, escalates the rest to a frontier LLM. Shows the tie on conventional metrics hides divergent unsupported-claim admission (23.2% vs 14.1%).

## Key results
> "routing the claims the cheap model is confident about and escalating the rest reaches 74.10 at USD 2.92 per thousand claims against 73.83 at USD 8.93, with the threshold chosen out of fold." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 1 · E 1 = 7 — A2 · B2 · C1 · D1 · E1 — 495 human-labelled LLM-AggreFact claims, within-item design; frontier LLM in the loop lowers D; cascade verifier is a new component.

## Affected axis
New-Techniques

## Relevance for RAG-NIMBF
Not expressible: no verifier-cascade slot in RAG-NIMBF → `new-axis.md`.
