# SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation (arxiv-2610.36991)

**Core idea:** Builds a weighted chunk graph (semantic similarity, document adjacency, section hierarchy, shared entities, citation links, LLM-generated utility questions), expands a hybrid seed set over the graph, re-scores via spectral relevance propagation, and assembles context under a fixed token budget.

**Key result (verbatim):** "Experiments on MultiHopRAG, UltraDomain, and long-document question-answering settings show that SpectRAG improves broad evi[dence coverage]" (Abstract; truncated at fetch)

**Rubric:** A=2 B=2 C=1 D=1 E=1 → 8/10. Graph RAG technique; three settings including MultiHopRAG; code unclear; per-chunk LLM utility questions add cost but feasible; graph retrieval not expressible in NIMBF.

**Affected axis:** New-Techniques
