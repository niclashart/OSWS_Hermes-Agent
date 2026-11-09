# New-axis proposal — arXiv:2611.05596

**Paper:** "RAGCompass: Generalizable Retriever Routing via Reranking" (arXiv:2611.05596) — vault note [[arxiv-2611.05596]], screened 2026-11-05, score 8/10.

## What the paper shows
Query-adaptive routing among multiple retrievers: a contrastively fine-tuned reranker scores each candidate retriever's evidence set against the answer it would produce, and a small comparison head picks the best retriever per query. Quote (Abstract): "RAGCompass improves answer F1 by 28% relative to the best fixed retriever, and outperforms fusion baselines, three query-only routers, and a prompted 8B language model."

## Why not expressible in RAG-NIMBF today
A RAG-NIMBF matrix runs *all* retriever configurations as separate grid points; there is no per-query selection among them. Per-query retriever routing needs a new component that fans a query out to several configured retrievers and chooses one at runtime — the grid abstraction cannot express "pick per query".

## What RAG-NIMBF would need
- Config key `retrieval_router: <none | <router-model>>` plus `retrieval_router_pool: [<retrieval config A>, <retrieval config B>, …]` (sub-configs referencing the existing retrieval axes).
- New component in `benchmark/retrieval.py`: a routing retriever that executes each pool member and applies the router's choice; results per member logged for cost analysis.
- Metrics: routing accuracy and per-arm usage next to the standard metrics.

## Estimated effort
Medium–large (~1–2 weeks): multi-retriever fan-out touches the run loop and caching; router itself can start as a prompted LLM baseline (paper: prompted 8B model already beats fixed retrievers) before a trained router.
