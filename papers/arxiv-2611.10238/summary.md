# CoRA-Bench: Evaluating Evidence Preservation by Context Selectors Under Token Budgets

arXiv 2611.10238

## Core idea
Benchmark comparing context-selection methods (truncation, BM25, dense, dense+rerank, LLMLingua-2, Provence) under *shared token budgets*, measuring evidence preservation (supporting-fact / needle / answer-bearing-turn recall) plus downstream reader accuracy on BABILong, LOONG, a NoLiMa diagnostic, and LongMemEval.

## Key results (verbatim)
> "BM25 achieves 0.921 supporting-fact recall on BABILong at 128K, dense retrieval and dense reranking each achieve 0.908 needle recall on NoLiMa at 64K, and dense retrieval achieves 0.993 answer-bearing-turn recall on LongMemEval at 64K." (Abstract)

> "At a 32K budget, BM25 achieves 46.20% BABILong answer accuracy and dense retrieval achieves 71.13% LongMemEval accuracy." (Abstract)

> "The results show that method rankings vary across evidence types and between evidence recall and downstream accuracy." (Abstract)

## Rubric
A 2 · B 2 · C 2 · D 1 · E 1 — 8/10 → relevant. Directly benchmarks the context-compression/selection axis RAG-NIMBF lacks; multi-dataset with CIs; benchmark public; hf-generic dataset adapter can load it but the budget-constrained selection protocol needs a new component (E=1).

## Affected axis
Evaluation / Datasets — candidate `hf-generic` dataset; the token-budget protocol itself is New-Techniques.

## Status log
- 2026-11-11 screened
