# EviCast: Forecasting Retrieval Gains Through Shared Response Calibration

- arXiv: https://arxiv.org/abs/2611.02387
- Screened: 2026-11-04 · Score: 8/10 · Rubric A-E: (2, 2, 2, 1, 1)
- Axis: Evaluation

## Core idea
Forecasts end-to-end net utility of RAG configurations before deployment by calibrating a generator's response to controlled evidence states once and combining with offline retriever evidence-state distributions — no full benchmark runs needed.

## Key results (verbatim quotes)
> "EviCast correctly decides all 14 HotpotQA retrieval configurations with a forecast error of 2.75 F1 points while reducing diagnostic generation calls by 80%." (Abstract)

## Rubric justification
A=2: pre-benchmark retrieval-value forecasting (Evaluation); B=2 14-24 configurations, theory + ablations; C=2 code; D=1 needs LLM generation calls; E=1 new pre-screening stage outside current config semantics.

## RAG-NIMBF relevance
Maps to the **Evaluation** axis; see vault note.
