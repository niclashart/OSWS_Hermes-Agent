# TRIO: Task Refinement with Individual Optimization for Retrieval-Augmented Generation

- arXiv: https://arxiv.org/abs/2611.02810
- Screened: 2026-11-04 · Score: 7/10 · Rubric A-E: (2, 2, 2, 1, 0)
- Axis: New-Techniques

## Core idea
Agentic RAG with three trained agents (query extension, unanimity judge, answer agent) aligned by individual optimization objectives and iterative refinement.

## Key results (verbatim quotes)
> "we first expand ambiguous queries with a query extension agent and quantify the reward based on the improved answer quality, which can be utilized to refine our agent for higher expansion efficiency." (Abstract)

## Rubric justification
A=2: agentic multi-agent RAG loop; B=2 multiple benchmark datasets; C=2 code released; D=1 training required; E=0: trained agent ensemble needs framework redesign — beyond MCP agentic tool use.

## RAG-NIMBF relevance
Not expressible as a single config value — new technique (see New-Techniques / New-Techniques).
