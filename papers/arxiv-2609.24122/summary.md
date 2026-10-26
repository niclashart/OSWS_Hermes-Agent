# Re:CAP - Auditing Retrieval Coverage in Production RAG Pipelines

**arXiv:** https://arxiv.org/abs/2609.24122 · **Score:** 8/10 (A2 B2 C1 D2 E0) · **Axis:** Evaluation · **Screened:** 2026-10-26

## Core idea
Reference-free audit loop that probes for missing topics and LLM-judge-filters newly retrievable docs; +12.9 pp recall on MuSiQue at less than half the document budget.

## Key results (verbatim quotes)
- "On MuSiQue Re:CAP beats flat hybrid top-500 by +12.9 pp on recall at less than half the document budget." (Abstract)
- "End-to-end recall is reproducible to within $\\pm$1% across three independent runs" (Abstract)

## Rubric justification
- A=2: coverage auditing by probing is a new evaluation technique
- B=2: MuSiQue +12.9 pp, TREC-COVID 48% gold recovery, human-annotated, reproducible within ±1%
- C=1: no code release stated
- D=2: probing loop with LLM judge, no GPU training
- E=0: needs audit-loop component outside matrix

## RAG-NIMBF fit
Not expressible; candidate for Evaluation new-axis (audit loop).
