# FinVeriQA: Financial Research Agents for Question Answering: Routing, Retrieval, MCP Tool Use, and Provenance-Aware Evidence Verification

arXiv: 2611.25071 · screened 2026-11-21 · score 8/10

## Core idea
An open-source multi-agent financial QA pipeline (FinVeriQA) over SEC filings and live market data in which each
component has a dedicated job: a small typed-decision model (Laya) routes questions and screens out advice
requests, Python computes every number (instead of the LLM), retrieval/tools fetch evidence, Mistral-7B writes a
cited answer, a code validator checks provenance (cited IDs exist, numbers match computed notes), and an MCP
server exposes the pipeline. The central finding is that provenance validation is not enough: verification must
be independent of the evidence the writer saw — a shared-evidence check catches far fewer corrupted-evidence
errors than a check against the original passage.

## Key results (verbatim quotes)
- "Laya routed better than Mistral-7B (0.85 vs. 0.52; overall 0.86 vs. 0.68, McNemar p=0.0003)" (Abstract)
- "Mistral-7B computed 29% of 100 financial calculations correctly against 100% for Python, a live quote cut price error from 210% to 0.00%, and hybrid retrieval reached 76% Hit@5 on 50 filing questions." (Abstract)
- "a shared-evidence check (the kind our validator performs) catches 35% of the errors, whereas a check against the original passage catches 77% (p=5.96×10⁻⁸); for DeepSeek-R1-8B, 68% vs. 90%." (Abstract)
- "when one figure in the shared evidence is corrupted, self-consistency stays confident (agreement 0.55 to 0.59 while accuracy falls from 0.50 to 0.00)" (Abstract)
- "Verified did not mean correct. The sentences match the sixth and seventh sample passages, so the content is grounded but the identifier is wrong ... The validator passed all of this because it checks _provenance_ ..., not _relevance_, _support_, or _coverage_." (Sec. 5.7)
- "The most consequential errors were not model errors: a table-of-contents stub that hid the risk factors, memory that leaked across companies, substring matching that refused harmless questions, a stale 'latest' filing, and a passage ID that pointed to the wrong text." (Sec. 6, Discussion)

## Rubric score: 8/10
- A 2 — agentic RAG system with typed routing, tool/MCP use, and provenance-aware verification; the
  independent-evidence verification requirement is a genuinely new evaluation technique.
- B 2 — live experiments with significance tests (McNemar), multiple baselines (Mistral-7B/12B,
  DeepSeek-R1-8B), plus a controlled upper-bound study on FinRank.
- C 1 — described as open-source, but license/repository access not verified in this screening.
- D 2 — 7B–8B models (Mistral-7B, DeepSeek-R1-8B), runnable on consumer GPU / Ollama; router is a compact model.
- E 1 — a provenance/independent-evidence verification metric and a route→compute→retrieve→write→validate
  chain are not expressible in RAG-NIMBF today (agentic MCP mode exists, but no verification stage or
  component-routing axis); needs a new component/metric.

## Affected axis
New-Techniques (agentic component routing + provenance-aware, source-independent verification; also touches
RAG-System MCP agentic mode and Evaluation metrics).
