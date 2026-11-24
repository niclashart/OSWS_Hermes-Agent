# GRACE: Controlled Evidence Interventions for Diagnosing and Improving Knowledge Integration in GraphRAG

arXiv: 2611.27350 · Screened: 2026-11-24 · Score: 8/10

## Core idea
A controlled-evaluation benchmark for GraphRAG: executes LC-QuAD 2.0 queries over Wikidata and applies four interventions to each evidence subgraph (sever support path, add type-compatible distractors, attach high-degree hubs, replace answer with counterfactual). 4,028 questions, 20,140 question-graph pairs, five fixed evidence states. Also proposes QCFSE-SA (typed local + global attention + question-conditioned evidence guidance with a calibrated graph-support gate).

## Key results
> "it improves controlled-state accuracy from 57.17% to 62.78% (+5.61 points; question-clustered 95% CI [+5.04, +6.17]) and broken-state accuracy from 55.41% to 67.85%." (Abstract)
> "question-only routing cannot distinguish evidence states, while relevance guidance can improve answerable states yet hurt when the support path is severed" (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 1 · E 0
A=2: new evaluation protocol for GraphRAG (Evaluation axis relevance) + graph retriever; B=2: controlled interventions, CI, ablation-like state comparisons; C=1: benchmark release claimed but license/code not stated in abstract; D=1: KG-RAG over Wikidata, model details unclear, likely heavy; E=0: RAG-NIMBF has no graph retrieval support nor evidence-intervention evaluation harness.

## Affected axis
New-Techniques (Graph RAG + controlled evidence-state evaluation)

## Status log
- 2026-11-24 screened (score 8)
