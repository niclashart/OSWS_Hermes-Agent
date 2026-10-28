# QESChunker: A Single Objective Unifies Overlapping and Non-Overlapping Chunking for RAG (arxiv-2610.36557)

**Core idea:** First supervised chunker: builds document-specific static chunk indices by maximizing question-evidence utility from human- or LLM-generated pairs. Non-overlap is solvable exactly by dynamic programming; the overlapping case is monotone submodular, optimized with a (1-1/sqrt(e))-approximation greedy.

**Key result (verbatim):** "Across two self-constructed and three public datasets, both variants outperform existing chunking methods in complete-evidence recall in nearly all evaluated settings, under the same overlap regime and a fixed hybrid retriever." (Abstract)

**Rubric:** A=2 B=2 C=1 D=2 E=1 → 8/10. Clear new chunking option; five datasets, same-overlap comparison; code/license unclear; static index construction, no retriever training; not a pluggable chunker value today — new chunker component needed.

**Affected axis:** Chunking
