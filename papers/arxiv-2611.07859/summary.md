# CORE: Coarse-to-Fine Search with Context Management for Deep Research (arXiv-2611.07859)

**Core idea.** Training-free deep-research harness: dense retrieval over long passages, then reuse the late-interaction (ColBERT) reranker's token-similarity matrix to extract only the highest-scoring snippet per passage; context management adds context expansion around already-retrieved sources and cross-search snippet deduplication.

**Key results.**
> "In controlled closed-search comparisons with the Tongyi DeepResearch and OpenResearcher harnesses, CORE achieves state-of-the-art answer accuracy and evidence recall across three agent models and three benchmarks" (Abstract); on BrowseComp-Plus with GPT-5.4: accuracy 94.94 vs 91.45 (OpenResearcher) and 84.70 (Tongyi), evidence recall 94.47 vs 89.55/81.53 (Sec. 4.2, Table).
> "Because snippet selection reuses the similarity matrix computed during passage reranking, it does not require any additional encoding." (Sec. 3.2)

**Rubric.** A 2 (context compression/selection under token budget + agentic search — explicitly on the not-expressible list) · B 2 (3 benchmarks, 3 agent models, controlled comparisons, component analysis) · C 1 (training-free method; code release not confirmed in abstract) · D 2 (retriever + ColBERT reranker, consumer-feasible) · E 1 (needs new context-management/snippet-selection component) = **8/10, relevant**.

**Affected axis:** New-Techniques (context compression + agentic search harness; RAG-NIMBF cannot express snippet selection, context expansion, or dedup today).

**Source:** https://arxiv.org/abs/2611.07859
