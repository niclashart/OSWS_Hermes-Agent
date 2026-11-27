---
id: arxiv-2611.31266
title: "Agentic Systems Need Multi-Run Evaluation: A Study of Retrieval and Response Variability in a Deployed Enterprise RAG System"
authors: [Karan Gupta, Sumit Bhatia, Yunyao Li]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 1, E: 1}
axis: [Evaluation, RAG-System]
status: screened
screened: 2026-11-27
source: https://arxiv.org/abs/2611.31266
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.31266/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.31266/summary.md
tags: [rag-radar, Evaluation]
---
# Agentic Systems Need Multi-Run Evaluation

**Axis:** [[Evaluation]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.31266) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.31266/paper.pdf)

## Core idea
Runs 739 questions ten times through a deployed agentic RAG system and shows single-run evaluation hides reliability issues: retrieval hit rate is 69.4% any-run vs. 50.9% every-run (18.5 pp). Trace alignment attributes divergence to steps — retrieval dominates (43.9%), the round-1 parallel-search count alone 20.1%.

## Results
> "the retrieval hit rate is 69.4% when the correct page is found in at least one run, but 50.9% when it must be found in all ten." (Abstract)

> "retrieval is the largest source of divergence (43.9%), and the number of parallel searches at the first retrieval step alone accounts for 20.1% of divergent pairs." (Abstract, Table 1)

> "average BERTScore of 0.90 and a BLEU of 0.49" — the behavioral consistency gap (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 1 · E 1 — new multi-run Evaluation protocol; 7,390 runs; no code/data release; needs deployed agentic system + LLM judges; RAG-NIMBF has no run-repetition axis.

## Relevance for RAG-NIMBF
A `benchmark_runs` setting with any-run/every-run aggregation of existing hit@k / gold-doc metrics; most relevant for `mcp_execution_mode: agentic` runs where sampling causes variability.

## Status log
- 2026-11-27 screened
