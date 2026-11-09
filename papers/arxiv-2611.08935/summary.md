# SkinMind: Equipping Agentic RAG with Human-Inspired Graph Probing for Reliable Dermatology AI

- arXiv: https://arxiv.org/abs/2611.08935
- Score: 8/10 · Axis: RAG-System · Verified: yes (export.arxiv.org, title match)

## Core idea
Multimodal agentic RAG: an orchestrator policy model iteratively probes a knowledge-graph environment through eight hierarchical graph-probing tools (entity identification, node inspection, relation/path traversal, source-text and visual evidence retrieval), building a query-specific evidence subgraph. SkinMind-KG is built from 62M tokens of dermatology text and 423K images (1.0M nodes, 2.0M edges); retrieval uses Qwen3-Embedding-4B, orchestration via GPT-5.4-mini / Gemini-2.5-Flash.

## Key results (verbatim)
> "SkinMind improves the average score over direct answering by 8.70 and 8.89 points with GPT-5.4-mini and Gemini-2.5-Flash, respectively, while consistently outperforming competing RAG methods." (Abstract)

> "Across six dermatology VQA benchmarks spanning morphology recognition, disease diagnosis, and clinical reasoning in both closed- and open-ended settings ... it surpasses LightRAG by an average of points with GPT-5.4-mini and points with Gemini-2.5-Flash." (Sec. 1)

License of the paper: CC BY-NC-ND 4.0. No public code/weights release is stated for SkinMind itself (only a baseline repo link, DermoGPT).

## Rubric
A 2 · B 2 · C 0 · D 0 · E 1 — A: agentic graph-probing RAG, clearly novel; B: six benchmarks, two policy models, ablations; C: no code/weights, NC-ND license, proprietary APIs required; D: relies on GPT-5.4-mini/Gemini APIs and a 4B embedder + massive KG build; E: graph retrieval = new axis, but closed-source makes integration moot.

## Affected axis
New-Techniques — graph probing / progressive disclosure is not expressible in RAG-NIMBF (Graph RAG is on the not-expressible list); RAG-System agentic adapter (MCP agentic) is the nearest existing mechanism.

## Status log
- 2026-11-09 screened
