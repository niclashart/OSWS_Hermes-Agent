# IndoNutriQA: An Indonesian Clinical Nutrition Question Answering Benchmark

- **arXiv:** https://arxiv.org/abs/2610.31256
- **Score:** 7/10 (A: 2, B: 2, C: 2, D: 2, E: 0) — open data and code (github.com/NLP-UB/IndoNutriQA), multi-baseline experiments incl. RAG, consumer-feasible
- **Axis:** Datasets

## Core idea
Expert-curated Indonesian clinical-nutrition QA benchmark: 911 QA pairs from 120 real reports, chunk-segmentation metadata, RAG baselines, LLM-as-judge calibrated against three expert raters.

## Key results (verbatim quotes)
> "every pair is grounded in a clinically relevant context, enriched with structured metadata (anthropometric assessment, medical diagnosis, document provenance, chunk segmentation)" (Abstract)

## RAG-NIMBF relevance
New dataset with chunk metadata; needs a registered dataset adapter in RAG-NIMBF. Weekly-fit candidate (new dataset value).
