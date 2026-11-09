# New-axis proposal — arXiv:2611.03725

**Paper:** "From Logs to Faults: Reference-Free Fault Localization for Retrieval-Augmented Generation Pipelines" (arXiv:2611.03725, RAGLog) — vault note [[arxiv-2611.03725]], screened 2026-11-07, score 9/10.

## What the paper shows
An LLM reads the structured execution log of a RAG pipeline run and localizes the faulty stage without reference answers. Quote (Abstract): "RAGLog achieves a pooled F1 score of 0.73 on runs with naturally occurring faults, outperforming Claude Code (0.58) and Codex (0.52) … It analyzes runs in approximately five seconds at US$0.005 each."

## Why not expressible in RAG-NIMBF today
RAG-NIMBF evaluates answer/retrieval quality (RAGAS, custom metrics) but has no diagnostic layer: a failed run yields scores, not a localization of *which* stage (loader/chunker/embedder/retriever/reranker/prompt/LLM) caused the regression. There is no config key or component for post-run fault analysis.

## What RAG-NIMBF would need
- Config key `fault_localization: <none | llm>` (settings) plus a `benchmark/diagnostics.py` component that consumes the per-run log/checkpoint artifacts (already persisted via `benchmark/checkpoint.py`) and outputs a ranked list of suspect stages.
- Output side-by-side with metric means in the run report so a score drop is immediately attributed.
- Judge model reuse: `eval_critic_llm` can serve as the localization LLM.

## Estimated effort
Small–medium (~3–5 days): log format already exists (checkpoints); work is the prompt pipeline, report integration, and a labeled-fault test fixture.
