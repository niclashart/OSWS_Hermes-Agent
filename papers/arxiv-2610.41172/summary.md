# Context as Infrastructure: Knowledge Compilation for Retrieval in Agentic Systems with Harnesses

arXiv 2610.41172 · Score 7/10 · Axis: New-Techniques

## Core idea
Agentic retrieval harnesses (query → read → reformulate → stop) have largely solved accuracy; the bottleneck is context discipline. Proposes "knowledge compilation" at ingestion: navigation trees whose leaves are claim–evidence pairs, plus entity graphs, timelines, ontologies, implemented in RAGFlow (open source). Compilation is a supply/token-cost layer, not an accuracy layer.

## Results
> "a harness whose only retrieval tools are BM25 and grep, with MiniMax M3 as the answering model, answers 85% of BrowseComp-Plus and reaches 91% on the multi-hop FRAMES benchmark … without any compiled index and without any vector index" (Sec. 1)
> "A navigation tree whose leaves are claim–evidence pairs … cuts total query tokens by 91% when the evidence suffices and adds 1.9% when it does not, for a 38% average reduction" (Sec. 4)
> "the decision gate reduced mean end-to-end latency from 140 s to 30 s, and the gate arm of Table 4 shows −52% tokens against the uncompiled baseline" (Sec. 8.5)
> "structural artifacts gave no detectable accuracy gain on FRAMES, and a PageIndex-style outline degraded at scale" (Sec. 8)

## Rubric
A 2 (context compilation / token-budgeted supply layer — clearly not expressible today) · B 2 (FRAMES + BrowseComp-Plus, with/without-artifact arms, measured token/latency effects) · C 2 (RAGFlow open source) · D 1 (harness needs a capable LLM; MiniMax M3 class) · E 0 (requires framework redesign: ingestion-side compilation artifacts + an agent harness loop, both new components)

## Relevance for RAG-NIMBF
Not expressible: context compression/selection under a token budget is listed under "Not expressible today". Needs `new-axis.md` in the weekly fit check (e.g. ingestion compilation + agent context budget axis).

## Status log
- 2026-11-02 screened
