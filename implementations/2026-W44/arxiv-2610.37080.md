---
paper: arxiv-2610.37080
week: 2026-W44
rag-nimbf: {verdict: missing, ref: main@f4b01f6}
blueprint: {verdict: partial, ref: feat/mcp-integration@c5780df}
---

# Tessera: Structure-Completed Evidence Units for Web Retrieval-Augmented Generation

## Why — evidence

> "Across three question answering benchmarks, Tessera improves answer accuracy by 5 to 6 points on
> text and screenshot pipelines, consistently across readers, retrievers, and reader budgets"
> (Abstract)

Rebuilds retrieved pages into fine-grained evidence units completed with page title, section path,
and table headers, then packs query-relevant units into the reader context. Training-free, +5-6 pp
accuracy across readers/retrievers. Score 8/10. https://arxiv.org/abs/2610.37080

## Existence check

Commands run:
- `git -C .cache/repos/RAG-NIMBF grep -n -i -E 'chunk.?graph|spectral|evidence.?unit|token.?budget|multi.?hop' main -- '*.py' '*.yaml'`
- `git -C .cache/repos/RAG-NIMBF show main:benchmark/chunking.py` (STRATEGY_MAP, `get_chunker`)
- `git -C .cache/repos/Enterprise_RAG_Blueprint grep -n -i -E 'chunk' main feat/mcp-integration -- 'loader/*.py'`

| repo | ref@sha | verdict | evidence |
|---|---|---|---|
| RAG-NIMBF | main@f4b01f6 | missing | `chunking.py` STRATEGY_MAP has recursive/character/token/markdown/text/transformers/paragraph/semantic. No post-retrieval structure completion, no evidence-unit delivery, no reader-budget packing. Also a fit-check gap (new Chunking value + delivery stage). |
| Blueprint | feat/mcp-integration@c5780df | partial | `loader/vector_store.py` chunks raw document text before embedding; no section-path/header metadata is preserved or restored at read time. Blueprint loads user-uploaded files, not web pages, so the HTML-rebuild part is out of scope — but the metadata enrichment idea could apply to markdown uploads. |

## Proposal: RAG-NIMBF

### Design

Add an **evidence-unit post-retrieval enrichment stage**: after `retrieve()`/`_rerank()` returns
chunks, a configurable `context_enrichment` step prepends each chunk's stored structural metadata
(`section_path`, headers, title) to the chunk text before generation. Tessera's full pipeline
(HTML rebuild of fetched pages) applies to web corpora; for RAG-NIMBF datasets the equivalent is
enriching chunks with the structure already present in metadata at index time.

This needs:
1. **Index-time**: a `structure` chunking strategy that splits on markdown headers and records
   `section_path` in chunk metadata (extending `benchmark/chunking.py`).
2. **Query-time**: `settings.context_enrichment: bool` in config; when true, the internal adapter
   prefixes `[<title> > <section_path>]` to each retrieved chunk before context assembly.

Effort: **M** (two stages, plus validation that Chroma metadata round-trips `section_path`).
Risks: token overhead per context (~5-10%); datasets without structural metadata fall back to
no-op; the paper's 5-6 pp gain was measured on web-page corpora, so the transfer to SQuAD-style
datasets is uncertain — that uncertainty is exactly what the grid would resolve.

Because the proposal spans a new chunking strategy AND a new settings flag AND adapter changes,
it is deferred to the weekly fit check as a candidate rather than fully specified here — the
existence check verdict stands: **missing** in RAG-NIMBF, not expressible with current axes.

## Proposal: Enterprise_RAG_Blueprint — not proposed

`partial`: the loader (`loader/vector_store.py`) could preserve section headers as metadata for
markdown/PDF uploads, but the Blueprint ingests internal user documents, not web pages; the
Tessera pipeline's core (web-page structure completion) is not applicable. A lightweight variant
(header-aware chunking for markdown uploads) is possible but the paper provides no direct evidence
for that setting.
