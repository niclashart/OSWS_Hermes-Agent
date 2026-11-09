# New-axis proposal — arXiv:2610.31019

**Paper:** "Chunk Recomputation under Real Document Revisions: Measuring Update Cost and Retrieval Quality of Fixed, Recursive, and Content-Defined Chunking" (arXiv:2610.31019) — vault note [[arxiv-2610.31019]], screened 2026-10-23, score 8/10.

## What the paper shows
The paper measures how much of a document's embedding workload must be recomputed after a real revision, per chunking strategy. Quote (Abstract): "fixed-size chunking recomputes 57–68% of its full new-version embedding-input workload, recursive chunking 38–56%, and content-defined chunking 43–54% ... while at these parameters mean evidence recall under a fixed 2048-token retrieval budget differs by less than two percentage points within either language".

## Why not expressible in RAG-NIMBF today
RAG-NIMBF evaluates chunking (`matrix.chunking_strategies`, `chunk_sizes`, `chunk_overlaps`) on a static index only. Two things are missing:

1. **A new chunking-strategy value** — content-defined chunking (CDC). The paper uses the
   Steadlith implementation (https://github.com/satwiksps/steadlith, Apache-2.0, pinned commit
   74c5b55b), word-level Rabin fingerprints with min/max length bounds. This part is nearly
   expressible: `chunking_strategies: [content-defined]` plus settings for min/max chunk length.
2. **A new evaluation dimension** — update cost. The benchmark must ingest a document, index it,
   ingest a revised version, and report the recompute fraction (byte-identical reuse of complete
   embedding inputs) alongside retrieval quality. RAG-NIMBF has no revision-pair ingestion,
   no previous-version chunk cache, and no `recompute_fraction` metric.

## What RAG-NIMBF would need
- New config keys (settings):
  - `chunking_strategies` value `content-defined` (+ `settings.cdc_min_chunk_tokens`, `cdc_max_chunk_tokens`)
  - `settings.update_eval_mode: <off|revision-pairs>` and `settings.update_eval_corpus: <path to revision-pair dataset>`
- New component: a previous-version embedding-input cache per document (keyed by exact byte-identical chunk text), used only in update-eval mode.
- New custom metric: `recompute_fraction` (tokens of new-version embedding inputs absent from the previous-version cache / total new-version embedding-input tokens), reported next to nDCG/recall in MLflow.

## Estimated effort
- CDC strategy value (wrapping Steadlith): small (~1–2 days, one adapter class in `benchmark/chunking.py`).
- Revision-pair ingestion + reuse cache + metric: medium (~1–2 weeks: dataset loader for revision pairs, cache lifecycle across benchmark stages, metric wiring, tests). No framework redesign; it composes with the existing Chunking and Evaluation axes.
