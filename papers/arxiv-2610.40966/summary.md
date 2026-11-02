# Better Retrievers, Worse Labels: How Incomplete Relevance Judgments Distort Abstention Evaluation in Conversational RAG

arXiv 2610.40966 · Score 9/10 · Axis: Evaluation

## Core idea
Conversational-RAG benchmarks (MTRAG, RETECO/RECOR) score abstention by reading sufficiency off relevance judgments ("no gold document → unanswerable"). This shortcut breaks as retrievers improve: better retrieval finds the answer in contexts without gold documents, so refusal scoring becomes wrong.

## Results
> "The stronger the retriever, the larger the share of no-gold contexts that still contain the answer (28% to 72%) and the lower the shortcut's precision (.68 to .10; .70 to .21 under the audit)." (Abstract / Sec. 4)
> "On MTRAG, whose judgments come from annotators, precision drops from .72 to .50. Under the shortcut, answerability AUROC is up to .19 too low, and the best sufficiency detector appears to be a retrieval score that never reads the documents." (Sec. 4)
> "Qwen3-4B answers 62–67% of these false misses correctly" (Abstract)

## Rubric
A 2 (evaluation-protocol finding, directly the Evaluation axis) · B 2 (RECOR + MTRAG, 4 retrievers spanning nDCG@10 .18–.59, 3 readers, LLM judges + blind audit with adjudication) · C 2 (code, runs and labels released) · D 2 (open Qwen3 readers + small judge panel) · E 1 (framework change is metric/label handling, not a config value; needs content-based sufficiency labels)

## Relevance for RAG-NIMBF
Evaluation axis: abstention/refusal metrics must be scored against content sufficiency labels, not gold-document presence. Affects `custom_metrics` (refusal detection) and gold-doc based metrics interpretation. Not a single config value → likely `new-axis.md`.

## Status log
- 2026-11-02 screened
