---
id: arxiv-2611.25071
title: "FinVeriQA: Financial Research Agents for Question Answering: Routing, Retrieval, MCP Tool Use, and Provenance-Aware Evidence Verification"
authors: [Meenakshi Rajpurohit, Anna Phan, Ravikumar Komandur Narayanan, Gunanidhi Ramakrishnan, Nathan Howland]
year: 2026
score: 8
rubric: {A: 2, B: 2, C: 1, D: 2, E: 1}
axis: [RAG-System, Evaluation]
status: screened
screened: 2026-11-21
source: https://arxiv.org/abs/2611.25071
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.25071/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.25071/summary.md
tags: [rag-radar, rag-system, evaluation]
---
# FinVeriQA: Financial Research Agents for Question Answering

**Axis:** [[RAG-System]] · **Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.25071) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.25071/paper.pdf)

## Core idea
Multi-agent financial QA prototype over SEC filings and live market data where each job goes to a dedicated
component: a compact typed-decision model (Laya) routes questions, Python computes every number, retrieval/tools
fetch evidence, Mistral-7B writes a cited answer, a code validator checks provenance, and an MCP server exposes
the pipeline. Central finding: provenance validation is insufficient — verification must be independent of the
evidence the writer saw.

## Results
> "Laya routed better than Mistral-7B (0.85 vs. 0.52; overall 0.86 vs. 0.68, McNemar p=0.0003)" (Abstract)
> "Mistral-7B computed 29% of 100 financial calculations correctly against 100% for Python, a live quote cut price error from 210% to 0.00%, and hybrid retrieval reached 76% Hit@5 on 50 filing questions." (Abstract)
> "a shared-evidence check (the kind our validator performs) catches 35% of the errors, whereas a check against the original passage catches 77%" (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — agentic routing + tool use + provenance verification with significance-tested
multi-baseline experiments on 7–8B models; but the verification stage and component routing are not
expressible in RAG-NIMBF today.

## Relevance for RAG-NIMBF
MCP agentic mode (`rag_system_adapter: mcp`, `mcp_execution_mode: agentic`) covers part of the pipeline
pattern, but there is no component-routing axis and no provenance/independent-evidence verification metric —
likely [[New-Techniques]].

## Status log
- 2026-11-21 screened
