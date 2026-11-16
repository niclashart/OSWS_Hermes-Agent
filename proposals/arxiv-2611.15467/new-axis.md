# New-axis proposal — arXiv:2611.15467

**Paper:** "AutoOntic: Automatic Ontology Induction from Text for Knowledge Graph Construction" (arXiv:2611.15467) — vault note [[arxiv-2611.15467]], screened 2026-11-13, score 8/10.

## What the paper shows
Automatically induces an ontology (canonical types/relations, is-a hierarchy, domain/range constraints) from schema-free LLM extractions and uses the hierarchy to gate entity deduplication. Quote (Abstract): "On MINE, knowledge graphs organized using an ontology built by AutoOntic achieve 88% retrieval accuracy."

## Why not expressible in RAG-NIMBF today
Graph RAG / knowledge-graph retrieval is listed as not expressible; AutoOntic sits even earlier in the pipeline (KG construction quality), and RAG-NIMBF has no ingestion-time ontology-induction stage, no entity-deduplication knob, and no KG-retrieval-accuracy metric.

## What RAG-NIMBF would need
- Graph ingestion plugin with a toggle `kg_ontology: none | autoinduced | fixed` before extraction/dedup.
- Retrieval-accuracy metric on KG-organized corpora; Text2KGBench subsets + MINE as dataset adapters.
- Code is open (github.com/screemix/AutoOntic, license to verify before any integration); runs with ordinary LLM backbones.

## Estimated effort
Large (~2–3 weeks), dominated by the graph adapter itself (see also arXiv:2611.11010 proposal — a graph-RAG base adapter would serve both papers).
