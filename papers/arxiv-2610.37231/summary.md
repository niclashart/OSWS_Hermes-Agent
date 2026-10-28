# TaskBridge: Technical Report for SIGIR 2026 eCommerce Challenge (arxiv-2610.37231)

**Core idea:** Reformulates task-oriented queries into product-retrieval expressions by grounding them in catalog vocabulary: Catalog Semantic Anchoring, Unified Five-Candidate Rewriting, and Protocol-Aware Selection, followed by BM25 retrieval.

**Key result (verbatim):** "These queries often imply product needs through activity-level semantics, creating a lexical gap with catalog descriptions." (Abstract, motivation)

**Rubric:** A=2 B=1 C=1 D=2 E=1 → 7/10. Query rewriting clearly beyond HyDE; single challenge task; code unclear; LLM rewriting cheap on consumer hardware; multi-candidate rewriting/selection needs a new component.

**Affected axis:** Query-Transformation
