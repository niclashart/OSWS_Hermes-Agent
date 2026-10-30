# 2610.37826 — DeFT-RAG: Incrementally Decomposing Multi-Hop Questions into Self-Contained Sub-Questions with Reusable Answers

**Score:** 7/10 · **Axis:** Query-Transformation · [arXiv](https://arxiv.org/abs/2610.37826) · [HTML](https://arxiv.org/html/2610.37826)

## Core idea
DeFT-RAG decomposes multi-hop questions into self-contained sub-questions one at a time (each names every entity), keeps state in a rule-based QA table, offloads yes/no decisions to a small fine-tuned model, and caches QA pairs for reuse across questions.

## Key results (verbatim quotes)
> "With a QA cache shared across 1,000 MuSiQue questions, 23.1% of sub-questions are answered from the cache, which reduces LLM calls by 12.9% without lowering accuracy." (Abstract)

## Rubric score with justification
A 2 (iterative query decomposition + caching; not expressible) · B 2 (MuSiQue/2Wiki/HotpotQA, 13 baselines, 2 backbones) · C 1 (code release not confirmed in HTML) · D 2 (gpt-4o-mini and small backbone) · E 0 (needs iterative loop + QA cache component)

## Affected axis
Query-Transformation: Not expressible: query decomposition / multi-hop loops are explicit gaps. The QA-cache reuse idea is an additional new-axis candidate (cross-question caching).
