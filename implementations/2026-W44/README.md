# Implementation check 2026-W44

Candidates: papers with score >= 8 or `status: fit`, screened 2026-10-24..30, not checked before.
Refs: RAG-NIMBF `main@f4b01f6`; Blueprint `main@1bf76b7`, `Benchmark_Adaptions@b2a9851`,
`feat/mcp-integration@c5780df`.

| id | title | NIMBF verdict | Blueprint verdict | proposed | reason |
|---|---|---|---|---|---|
| 2609.38473 | Re-ranking and Late Interaction Drive Retrieval Quality (10/10) | partial (cross-encoder exists, no late interaction) | missing (no reranking at all) | **yes — both** | largest quality lever under fixed generator; colbert provider closes NIMBF gap; default-off reranking stage for Blueprint |
| 2609.24885 | The Copy Ceiling (9/10) | missing (no copy-baseline metric) | partial (per-request LLM check only) | **yes — NIMBF** | cheap evaluation-metric add-on in `custom_metrics.py`; Blueprint eval is per-request, not applicable |
| arxiv-2610.37080 | Tessera: Structure-Completed Evidence Units (8/10) | missing (new chunking strategy + delivery stage needed) | partial (header-aware chunking possible) | no — existence check only | spans new axis + adapter change; deferred to weekly fit check; Blueprint not a web-corpus system |
| arxiv-2610.36991 | SpectRAG: Weighted Chunk Graphs (8/10) | missing (no graph retrieval) | not-applicable | no — existence check only | graph retrieval not expressible in NIMBF (see nimbf-capabilities.md); LLM utility questions per chunk too costly for Blueprint |
| arxiv-2610.36650 | TACO-Graph: TAG Construction Search (8/10) | missing (no graph RAG support) | not-applicable | no — existence check only | requires a graph-construction axis in NIMBF; production system has no GraphRAG path |

Existence-check commands are recorded in the per-paper files.
