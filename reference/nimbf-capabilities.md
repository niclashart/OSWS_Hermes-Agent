# What RAG-NIMBF can express (fit-check reference)

Source: RAG-NIMBF `config.py`, `benchmark/chunking.py`, `experiments/full-grid-example.yaml`.
A paper is **expressible** if its technique maps to a value below (or a model ID that can be plugged
into an existing slot). Otherwise write `new-axis.md` instead of `config.yaml`.

| Axis (vault note) | YAML key | Supported values |
|---|---|---|
| Chunking | `matrix.chunking_strategies`, `chunk_sizes`, `chunk_overlaps` | `recursive`, `character`, `token`, `markdown`, `text`, `transformers`, `paragraph`, `semantic` (+ `settings.semantic_breakpoint_type/amount`) |
| Embedding | `matrix.embedding_models` | any Ollama embedding model or `sentence-transformers/<hf-id>` |
| Retrieval | `matrix.retrieval_strategy`, `retrieval_top_k` | `similarity`, `mmr`; integer top-k |
| Query-Transformation | `matrix.retrieval_use_hyde` | HyDE on/off (other query rewriting = new axis) |
| Reranking | `matrix.reranker_models` | `null` or `sentence-transformers/<hf-id>` cross-encoder / reranker |
| Prompting | `matrix.prompt_templates` | built-in templates (`concise`, `detailed`, …) |
| Generator | `matrix.llm_models` | `ollama:<model>`, `openai:<model>` (OpenAI-compatible endpoint) |
| Vector-Store | `settings.vector_db_backend` | `chroma`, `lancedb` |
| RAG-System | `settings.rag_system_adapter` | `internal`, `http`, `mcp`, `ragflow` (external systems via adapter) |
| Datasets | `dataset.name`, `dataset.sample_size` | registered adapters, e.g. `squad`, `ragas-wikiqa`, `ragbench`, `t2-ragbench` |
| Evaluation | `settings.eval_critic_*`, `custom_metrics_*` | RAGAS-style LLM-judge metrics, nDCG@k, BERTScore, runtime (MLflow) |
| Retrieval-Mode | `settings.retrieval_mode` | `retrieval`, `direct` (no retrieval baseline) |

Not expressible today (→ `new-axis.md`): graph RAG, agentic / multi-hop loops, self-reflective RAG,
query decomposition, hybrid BM25+dense, fine-tuned retrievers, long-context vs RAG trade-offs.
