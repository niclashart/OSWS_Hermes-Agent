# RAG-TRACE: Tracing Measurement Evidence and Diagnostic Completeness in AI-Generated ECG Reports

- arXiv: https://arxiv.org/abs/2611.01409
- Screened: 2026-11-04 · Score: 7/10 · Rubric A-E: (2, 2, 1, 1, 1)
- Axis: Evaluation

## Core idea
Shows retrieved diagnostic criteria in RAG-generated ECG reports often lack patient-specific measurement support; retrieval increased unsupported-criterion reports; deterministic measurement verification removes most unsupported applications.

## Key results (verbatim quotes)
> "Under matched instructions and an identical output schema, retrieval increased unsupported-criterion reports from 17.4% to 31.1%, while hypertrophy recall remained unchanged at 62.6%." (Results, Abstract)

## Rubric justification
A=2: evidence-support verification as an evaluation dimension — retrieval can hurt factuality (Evaluation); B=2 1,083 records + controlled experiments; C=1 no code mentioned; D=1 API models; E=1 new criterion-support metric needed.

## RAG-NIMBF relevance
Maps to the **Evaluation** axis; see vault note.
