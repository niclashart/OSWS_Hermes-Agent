# AutoOntic: Automatic Ontology Induction from Text for Knowledge Graph Construction

- arXiv/HF id: arxiv-2611.15467
- Score: 8/10 (A 2, B 2, C 1, D 2, E 1)
- Date screened: 2026-11-13
- Axis: New-Techniques
- Source: https://arxiv.org/abs/2611.15467

## Core idea
AutoOntic builds an ontology (canonical types/relations, is-a hierarchy, domain/range constraints) from schema-free LLM extraction output, using the hierarchy to gate entity deduplication; released at github.com/screemix/AutoOntic.

## Key results (verbatim quotes)
> "On MINE, knowledge graphs organized using an ontology built by AutoOntic achieve 88% retrieval accuracy." (Abstract)

## Rubric justification
A 2 · B 2 · C 1 · D 2 · E 1 — graph-RAG KG construction technique; evaluated on Text2KGBench subsets + MINE; code open (license to verify at fit check), runs with ordinary LLM backbones; needs a new graph-ingestion component.

## RAG-NIMBF fit
Not expressible: Graph RAG / knowledge-graph retrieval is listed under 'Not expressible today' → new-axis.md candidate.
