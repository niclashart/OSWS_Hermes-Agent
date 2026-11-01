# caveman-so/trim-1 — model summary

- **Type:** HF reranker/context-compression model (712 gradient-boosted trees, 1.2 MB), apache-2.0
- **Slot:** `reranker_models: huggingface:caveman-so/trim-1` (nominally; really an extractive context compressor)
- **mteb:** (none)

## Core idea
trim-1 decides which lines of a context (tool result, file, log) an agent needs for the current query and drops the rest. Each line gets 67 numeric features (BM25 vs. query, line-kind detection, position/shape, neighbours); LightGBM trees produce a keep probability; an operating point (conservative/balanced/aggressive) selects lines plus block headers. Extractive: kept lines are verbatim, order preserved.

## Reported results (quotes from model card)
- "**1.2 MB.** 712 gradient-boosted trees, not a neural network." — "Milliseconds on one CPU core."
- "It saves the most on long-document retrieval, where it removes most of the input and keeps the evidence."
- Evaluation: "One run on 2026-10-11, on frozen holdout splits of public suites." A case passes "when every piece of labelled evidence is still in the output"; cut = share of tokens removed.
- "trim-1 fails closed. It returns the context unchanged when the query is blank, the context is under 2,000 bytes, …"

## Rubric
A 2 — context compression / budgeted selection under a token budget: a RAG technique RAG-NIMBF cannot express (explicitly listed as not expressible).
B 1 — single run on public suites measuring evidence-kept/cut, no end-to-end RAG answer-quality numbers.
C 2 — apache-2.0 code (github.com/caveman-ai/trim-1) + weights.
D 2 — 1.2 MB, CPU, milliseconds, deterministic.
E 1 — new component (line-level context compressor between retrieval and prompt), not a cross-encoder reranker.

## Affected axis
New-Techniques — context compression / selection under a token budget (new-axis candidate for the weekly fit check).
