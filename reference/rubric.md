# Relevance rubric (0–10)

Score each criterion, sum = total. **Total >= 7 → relevant** (PDF + summary + vault note).
Below 7 → only a row in `screening.csv`.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| A | Axis fit / novelty | unrelated to RAG pipelines | touches an existing RAG-NIMBF axis marginally | clear new option for an existing axis **or** new RAG technique (graph, agentic, self-reflective, …) that may need a new axis |
| B | Evidence quality | no experiments / only anecdotes | experiments on one dataset or weak baselines | multiple datasets, strong baselines, ablations |
| C | Reproducibility + license | no code, no model | code or weights, unclear license | code + weights under open license (MIT, Apache, CC-BY, …) |
| D | Feasibility on consumer GPU | needs > 48 GB VRAM or proprietary API only | runs with quantisation / small variant | runs on <= 24 GB VRAM or via Ollama |
| E | Integration effort into RAG-NIMBF | needs framework redesign | new component / adapter needed | config value or small plug-in (new reranker, chunker, embedder, prompt) |

## Notes
- Survey / position papers: A max 1, B = 0, unless they introduce a benchmark or dataset.
- New evaluation protocols / datasets: score A against the `Evaluation` / `Datasets` axes.
- HF models (`source: hf-model:embedder|reranker`, leaderboard watch): score from the model card (`abstract`) and the
  `mteb` link. A = 2 only if the card reports retrieval/reranking numbers that beat a model RAG-NIMBF users already run
  (e.g. bge-m3, bge-reranker-v2-m3, nomic-embed-text, Qwen3-Embedding/Reranker) or adds a clear capability
  (multilingual/German, long context, much smaller at equal quality); otherwise A <= 1. B: MTEB/BEIR results with
  baselines = 2, own unverified numbers = 1, none = 0. E = 2 only if loadable via sentence-transformers
  (`SentenceTransformer` / `CrossEncoder`) — late-interaction (ColBERT), LLM-listwise or multimodal rerankers = E 1
  (new provider). Domain-specific fine-tunes (legal, single non-English language except German) A max 1.
- GitHub releases: score only if the release adds a capability usable as a RAG-NIMBF axis value; otherwise 0 with reason `release: no new capability`.
- In `screening.csv` the `reason` column must name the decisive criterion, e.g. `E=0: requires training loop`.
