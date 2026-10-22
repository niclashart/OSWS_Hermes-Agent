# OpenSaC: A Python Library for Search as Code in Deep Research Agents (arXiv:2610.25779)

## Core idea
Search as Code paradigm: deep-research agents write programs composing search, source reading, reranking, model calls, and local processing, returning selected observations, instead of alternating reasoning with individual tool calls. OpenSaC is the open-source Python library + companion skill.

## Results
> "Compared with standard Codex using its built-in web search, the OpenSaC configuration uses less execution time and fewer model tokens on BrowseComp and WideSearch, with higher accuracy on BrowseComp and slightly lower row F1 on WideSearch" (Abstract). Code: https://github.com/liuqi6777/OpenSaC, CC BY 4.0.

## Rubric
A 2 · B 2 · C 2 · D 2 · E 0 — agentic programmatic retrieval loop, new technique; 2 benchmarks; open source; consumer-GPU via coding agents; needs whole new execution paradigm.

## Relevance for RAG-NIMBF
Not expressible: agentic retrieval control flow would need a new RAG-System adapter class (agent-driven), far beyond `internal/http/mcp/ragflow`.
