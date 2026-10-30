# 2610.34507 — The Price of Scale in Proactive Memory Recall

**Score:** 7/10 · **Axis:** New-Techniques · [arXiv](https://arxiv.org/abs/2610.34507) · [HTML](https://arxiv.org/html/2610.34507)

## Core idea
Shows that proactive memory recall (deciding whether anything in a growing store of N memories is worth surfacing) is a multiple-testing problem: a fixed false-alarm threshold loses control as N grows, with per-item false-positive rate ~ -ln(1-alpha)/N. Proposes a label-free cue-swap conformal gate with finite-sample false-alarm guarantees.

## Key results (verbatim quotes)
> "a similarity threshold tuned to 5% false alarms at N=8 reaches 87-100% at N=2048, across embedding models and for explicit and implicit cues" (Abstract)

## Rubric score with justification
A 2 (proactive recall gating: new technique) · B 2 (LongMemEval + LoCoMo, theory + experiments + annotation) · C 2 (code and data released) · D 2 (single RTX 3090) · E 1 (gate sits between retriever and generator; new component)

## Affected axis
New-Techniques: Not expressible: RAG-NIMBF always retrieves. A 'proactive gate' (retrieve or stay silent, N-dependent threshold) would be a new axis/setting, related to the retrieval_mode axis (retrieval/direct) but requiring a statistical gate.
