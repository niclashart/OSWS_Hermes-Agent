# Prevented is Not Protected: What Attack Success Rate Hides about RAG

arXiv 2610.40742 · Score 8/10 · Axis: Evaluation

## Core idea
ASR-only evaluation of RAG poisoning defenses hides defense-induced failures and mechanism. Proposes "Aligned RAG Evaluation": a matched-query protocol jointly examining clean and poisoned responses, with and without defense, combining matched-conditions analysis, LLM-judge endorsement, and retrieval-dependence controls.

## Results
> "Experiments on HotpotQA and Natural Questions reveal that existing defenses can introduce unexpected target-positive answers, although they can prevent some attacks, while evaluation criteria can also change defense rankings." (Abstract / Sec. 4)
> "the proposed framework distinguishes prevented from introduced failures, target mentions from LLM endorsement, and single-passage influence from evidence composition" (Abstract)

## Rubric
A 2 (new evaluation protocol for poisoning-defense evaluation, Evaluation axis) · B 2 (HotpotQA + NQ, multiple defenses, matched conditions, ablations) · C 2 (code and evaluation artifact released, MIT repo) · D 1 (victim models + LLM judges, feasible but multi-model) · E 1 (protocol-level change: matched clean/poisoned arms and endorsement judging are not single config values)

## Relevance for RAG-NIMBF
Evaluation axis: RAG-NIMBF currently has no knowledge-poisoning evaluation at all. Aligned evaluation would need poisoned-corpus arms + clean-utility arms + endorsement metric → `new-axis.md`.

## Status log
- 2026-11-02 screened
