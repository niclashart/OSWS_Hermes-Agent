# Structure-Exploiting Hierarchical Retrieval for Long Narrative Documents: A Precision-Oriented Alternative to Learned Abstraction Trees

arXiv: 2611.29966 · Screened: 2026-11-24 · Score: 8/10

## Core idea
Two-level coarse-to-fine retriever for book-length documents using native structure instead of RAPTOR's LLM-built hierarchy: (i) select chapters via hybrid BM25+dense match over chapter recaps, (ii) chapter-filtered dense search, (iii) expand top passages into section-aware spans under a token budget; plus content-hash-gated delta ingestion.

## Key results
> "On QuALITY, hierarchical retrieval significantly beats flat top-$k$ (81.0% vs 70.4%, $p{=}0.0019$) and is statistically indistinguishable from feeding the full article ($p{=}0.74$)" (Abstract)
> "with section expansion off, hierarchical retrieval returns a significantly higher fraction of chunks from the correct chapter (+3.3pp precision, Wilcoxon $p{=}0.014$)" (Abstract)
> "content-hash delta ingestion reuses 94–99.7% of embeddings on realistic incremental edits." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1
A=2: hierarchical structure-aware retrieval + delta ingestion is a new retrieval technique; B=2: three evaluation sets (in-house, QuALITY, NovelQA), flat and RAPTOR baselines, significance tests; C=1: reproducibility claimed but no code/license stated in abstract; D=2: BM25+dense, no heavy training, consumer-GPU feasible; E=1: hybrid BM25+dense fusion and chapter-level pre-selection are not in the internal adapter (no RRF fusion, no two-stage structural retrieval) — needs new retrieval component.

## Affected axis
New-Techniques (hierarchical retrieval, hybrid fusion not yet expressible)

## Status log
- 2026-11-24 screened (score 8)
