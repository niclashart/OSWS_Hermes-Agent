# Tessera: Structure-Completed Evidence Units for Web Retrieval-Augmented Generation (arxiv-2610.37080)

**Core idea:** Decouples retrieval from reading: rebuilds retrieved pages' HTML into fine-grained evidence units completed with page title, section path, and table headers, then packs query-relevant units into the reader context. Applies to text, screenshot, and agentic pipelines.

**Key result (verbatim):** "Across three question answering benchmarks, Tessera improves answer accuracy by 5 to 6 points on text and screenshot pipelines, consistently across readers, retrievers, and reader budgets" (Abstract)

**Rubric:** A=2 B=2 C=1 D=2 E=1 → 8/10. New evidence-unit option for the Chunking axis; full English Wikipedia, three benchmarks, matched-budget baselines; code unclear; training-free; needs a new post-retrieval delivery component.

**Affected axis:** Chunking
