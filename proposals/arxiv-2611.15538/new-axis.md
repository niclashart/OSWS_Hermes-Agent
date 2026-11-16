# New-axis proposal — arXiv:2611.15538

**Paper:** "Faithful in Steps: Improving Generalization and Citation in RAG via Query Decomposition" (arXiv:2611.15538) — vault note [[arxiv-2611.15538]], screened 2026-11-13, score 7/10.

## What the paper shows
QDRAG decomposes multi-hop questions into atomic subquestions and prunes distractor contexts with a reranker for faithful citations. Quote (Abstract): "significantly outperforms all the baselines on both in-domain and out-of-domain tests, even surpassing Gemini-Pro."

## Why not expressible in RAG-NIMBF today
Query decomposition / rewriting other than HyDE and multi-hop follow-ups is explicitly listed as not expressible. QDRAG's zero-shot decomposition modes (context-guided, retrieval-reward-guided, with a finetuned MLLM) are a different query-transformation family, and its citation-faithfulness evaluation has no counterpart among the RAGAS/custom metrics.

## What RAG-NIMBF would need
- Config key `query_transformation: none | hyde | decomposition` (+ `decomposition_mode`, `decomposition_prune_reranker`).
- Sub-question loop in the retrieval stage (retrieve per subquestion, merge, rerank-prune).
- Citation-faithfulness metric (quote-support check) in `custom_metrics.py`.

## Estimated effort
Medium (~1 week): the retrieval loop resembles the existing `retrieval_multihop` machinery; the new part is the decomposition prompt mode and the citation metric. No public code stated (C=1), so the decomposition prompt must be reimplemented from the paper.
