# New-axis proposal — arXiv:2611.02258

**Paper:** "Beyond Binary Detection: Type-Aware Hallucination Analysis and Hierarchical Detection in Financial Question Answering" (arXiv:2611.02258) — vault note [[arxiv-2611.02258]], screened 2026-11-07, score 8/10.

## What the paper shows
Hallucination evaluation at subtype level (nine types) on PHANTOM: a plain LLM detector reaches only 44.7% subtype accuracy; a two-stage hierarchical detector (binary first, then subtype) reaches 95.6% binary / 56.1% subtype. Quote (Abstract): "type-level evaluation exposes detector weaknesses that aggregate metrics conceal."

## Why not expressible in RAG-NIMBF today
Hallucination-specific metrics beyond RAGAS faithfulness are listed as not expressible (reference/nimbf-capabilities.md). RAG-NIMBF's custom metrics are fixed IR/NLG metrics; there is no slot for a taxonomy-based hallucination-subtype classifier or per-type breakdown.

## What RAG-NIMBF would need
- New custom metric plugin: `hallucination_subtype` — LLM-judge classifies each answer into the taxonomy (or "faithful"), reported as per-type precision/recall plus aggregate. The plugin mechanism (`custom_metrics_enabled`, metric registry) exists, so this is an extension, not a redesign.
- Config key `hallucination_taxonomy: <none | <path or name>>` to select the type set (financial, general, domain-specific).

## Estimated effort
Small (~3–4 days): one custom metric class following the existing `CustomMetricsResult` interface, a judge prompt, and per-type aggregation in the report.
