# New-axis proposal — arXiv:2610.37080 (Tessera)

**Paper:** "Tessera: Structure-Completed Evidence Units for Web Retrieval-Augmented Generation" (arXiv:2610.37080) — vault note [[arxiv-2610.37080]], screened 2026-10-28, score 8/10.

## What the paper shows
Decouples retrieval from reading: rebuilds retrieved pages' HTML into fine-grained evidence units completed with page title, section path, and table headers, then packs query-relevant units into the reader context. Training-free, applies to text, screenshot, and agentic pipelines. Quote (Abstract): "Across three question answering benchmarks, Tessera improves answer accuracy by 5 to 6 points on text and screenshot pipelines, consistently across readers, retrievers, and reader budgets."

## Why not expressible in RAG-NIMBF today
Tessera introduces a *post-retrieval evidence-unit layer*: the indexed/chunked representation stays as-is, but what is handed to the reader is rebuilt from the retrieved page's structure (title, section path, table headers) and packed under a budget. RAG-NIMBF has nothing between retrieval/reranking and the prompt except document count (`generation_context_k`); raw retrieved chunks go straight into the prompt. Chunking-axis values all operate at index time, not query time.

## What RAG-NIMBF would need
- New config stage `context_builder: <raw | evidence-units>` (+ `evidence_unit_budget` tokens, `evidence_unit_source: <html | markdown>`).
- New component: parse retrieved document metadata/raw HTML (needs the parser layer, `benchmark/parsing/`, to retain structure), rebuild evidence units with title + section path + table headers, and pack under budget — a `ContextBuilder` protocol analogous to `Reranker`.
- Dependency on `corpus_parser` (raw docs to Markdown) for the internal adapter, so structured evidence units can be rebuilt at query time.

## Estimated effort
Medium (~1–2 weeks): the packing logic is training-free and simple, but structure retention end-to-end (parser → index metadata → query-time rebuild) touches ingestion, retrieval payloads, and prompt assembly, plus tests.
