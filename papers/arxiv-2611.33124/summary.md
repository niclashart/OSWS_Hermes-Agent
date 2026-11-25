# SAG-Mem-1.0 Technical Report (arxiv-2611.33124)

**Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.33124)

## Core idea
Conversational long-term memory that keeps complete dialogue messages in non-overlapping chunks with a lexical (BM25) index — no LLM-based memory construction. At query time, an evidence evaluator scores initial BM25 candidates and lexical cues from selected evidence guide a second retrieval round; relative-time expressions get calendar annotations.

## Results
> "On LoCoMo and LongMemEval, SAG-Mem achieves overall scores of 83.08 and 80.20, respectively, the highest among the evaluated methods on both benchmarks. On LongMemEval, it exceeds the strongest compared baseline by 7.20 points." (Abstract)
> "Memory construction requires no model inference, using a lexical index without LLM-based extraction, summarization, or semantic relation construction." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 0 — clear new RAG technique (memory + iterative lexical expansion); two benchmarks with baselines; no code link stated; runs with small LLMs; but the technique (BM25 lexical index + evidence-guided second round) is not expressible in RAG-NIMBF (no BM25/hybrid in internal adapter, no evidence-evaluator loop).

## Relevance for RAG-NIMBF
New-Techniques: needs hybrid BM25 retrieval and an evidence-guided retrieval-expansion loop as new axis values.

## Status log
- 2026-11-25 screened
