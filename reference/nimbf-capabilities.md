# What RAG-NIMBF can express (fit-check reference)

Source: RAG-NIMBF `main@f4b01f6` (2026-10-30) — `config.py` (`BenchmarkConfig`), `benchmark/orchestration/matrix.py`,
`benchmark/chunking.py`, `benchmark/retrieval.py`, `benchmark/reranker.py`, `benchmark/providers.py`,
`benchmark/prompt_templates/`, `benchmark/dataset_adapters.py`, `benchmark/adapters/`, `benchmark/parsing/`,
`benchmark/custom_metrics.py`, `benchmark/gold_retrieval_metrics.py`, `benchmark/evaluation.py`, `examples/`.
For anything not listed here, check the live code (`git -C .cache/repos/RAG-NIMBF grep … main`) before deciding.

A paper is **expressible** if its technique maps to a value below (or a model ID that can be plugged
into an existing slot). Otherwise write `new-axis.md` instead of `config.yaml`.

## How experiment YAML works
- `settings:` and `matrix:` accept **any field of `BenchmarkConfig`**; unknown keys raise an error.
  Every `matrix:` key is a grid axis (list of values); `settings:` are fixed for all runs.
- Plural aliases in `matrix:`: `llm_models`, `embedding_models`, `chunking_strategies`, `chunk_sizes`,
  `chunk_overlaps`, `prompt_templates`, `reranker_models`, `dataset_names`, `parser_adapters`.
  All other axes use the field name directly (e.g. `retrieval_top_k`, `retrieval_strategy`, `retrieval_use_hyde`,
  `retrieval_multihop`, `generation_temperature`).
- `dataset:` block: `name`, `sample_size`, `subset`, `split`, `path`, `corpus_path`, `license`.
- Model IDs use `provider:model` — providers `ollama:`, `openai:` (OpenAI-compatible endpoint), `huggingface:`.
  **Unprefixed IDs default to Ollama**, so a bare `sentence-transformers/<id>` is treated as an Ollama model.
  Use `huggingface:<hf-id>` for HuggingFace embedders and rerankers.

## Axes
| Axis (vault note) | YAML key | Supported values |
|---|---|---|
| Chunking | `chunking_strategies`, `chunk_sizes`, `chunk_overlaps`, `semantic_breakpoint_type`, `semantic_breakpoint_amount` | `recursive`, `character`, `token`, `markdown`, `text`, `transformers` (sentence-transformers token splitter), `paragraph` (no size/overlap), `semantic` (breakpoint `percentile` / `standard_deviation` / `interquartile` + amount), `provider` (managed system chunks itself; `ingestion_method`, `ingestion_options_json`). Overlap must be < size. |
| Embedding | `embedding_models` | `ollama:<model>` (or bare Ollama name) or `huggingface:<hf-id>` (any sentence-transformers / HF embedding model) |
| Retrieval | `retrieval_strategy`, `retrieval_top_k`, `retrieval_fetch_k`, `retrieval_mmr_lambda` | `similarity`, `mmr` (fetch_k oversampling, lambda 0 = diversity … 1 = relevance); integer top-k |
| Retrieval (multi-hop) | `retrieval_multihop`, `retrieval_multihop_rounds` | iterative multi-hop retrieval: LLM generates a follow-up query per round, results merged (k split across rounds) |
| Retrieval (managed systems) | `retrieval_candidate_k`, `retrieval_similarity_threshold`, `retrieval_vector_similarity_weight`, `retrieval_keyword_enabled` | hybrid keyword + vector weighting, threshold, candidate pool — **only honoured by managed adapters** (`ragflow`, `optimaiserag`), not by `internal` |
| Query-Transformation | `retrieval_use_hyde` | HyDE on/off (multi-hop follow-up queries see above; other rewriting / decomposition = new axis) |
| Reranking | `reranker_models`, `reranker_top_k` | `null` or `huggingface:<hf-id>` cross-encoder (sentence-transformers `CrossEncoder`, e.g. `huggingface:BAAI/bge-reranker-v2-m3`). Only cross-encoders; late interaction (ColBERT) / LLM rerankers = new provider |
| Prompting | `prompt_templates` | `concise`, `detailed`, `minimal`, `no_context`, `cot`, `cited`, `abstain_strict`, `question_first`, `chain_of_note`, `finqa` |
| Generator | `llm_models`, `max_new_tokens`, `generation_temperature`, `generation_top_p`, `generation_presence_penalty`, `generation_frequency_penalty`, `generation_context_k` | `ollama:<model>`, `openai:<model>`; `llm_answer_strip_mode` (thinking-tag stripping) |
| Vector-Store | `vector_db_backend` | `chroma`, `lancedb` (`lancedb_path`) |
| RAG-System | `rag_system_adapter` (+ `rag_adapter_accepts`) | `internal`; `http` (answer-only endpoint); `mcp` (`mcp_result_mode` `context` / `answer`, `mcp_execution_mode` `fixed` / `agentic` with `mcp_max_agent_rounds`); `ragflow`, `optimaiserag` (managed lifecycle); plugins `enterprise_rag` and `enterprise_rag_mcp` (Enterprise_RAG_Blueprint, `examples/enterprise_rag_plugin`), custom plugins via env `RAG_ADAPTER_MODULES`. `rag_adapter_accepts` injects benchmark components (`chunker,embedder,retriever,reranker,llm,prompt`) into external systems |
| Datasets | `dataset.name`, `dataset.sample_size` | `squad`, `ragas-wikiqa`, `ragbench`, `t2-ragbench`, `ragperf-wikipedia-nq`, `multihop-generic`, `hf-generic` (any HF dataset via `dataset_question_field` / `dataset_ground_truth_field` / `dataset_context_field`), `jsonl`, `jsonl-shared` (shared corpus via `corpus_path`), `csv`; OCR ground truth: `omnidocbench`, `dp-bench`, `olmocr-bench` |
| Document-Parsing (OCR) | `benchmark_stage: parsing`, `parser_adapters`, `corpus_parser` | parser adapter `http` (vision-LLM endpoint) or plugin (`parser_plugin_module`); text metrics, table metrics incl. TEDS; `corpus_parser` parses raw docs to Markdown before chunking (needs `jsonl-shared`) |
| Evaluation | `ragas_enabled`, `eval_critic_*`, `custom_metrics_enabled`, `custom_metrics_bert_model`, `custom_retrieval_metrics_mode` | RAGAS LLM-judge: faithfulness, answer relevancy, answer correctness, context precision, context recall, semantic similarity. Custom: hit@k, nDCG@k, recall@k, context relevance, ROUGE-L, BLEU, METEOR, BERTScore P/R/F1, refusal detection, embedding distances. `custom_retrieval_metrics_mode`: `heuristic` or `gold_doc` (gold-document / span hit, MRR, nDCG, recall@k) |
| Retrieval-Mode / Stage | `retrieval_mode`, `benchmark_stage` | `retrieval`, `direct` (no-retrieval baseline); stages `all`, `index`, `query`, `retrieve`, `parsing` |
| Efficiency | `llm_performance_enabled`, `llm_performance_call_counts`, `llm_performance_source` | LLM load test (concurrency levels), runtime, token cost (`costing.py`), GPU/power monitoring, MLflow / ClearML tracking |

## Not expressible today (→ `new-axis.md`)
Graph RAG / knowledge-graph retrieval, hybrid BM25 + dense fusion (RRF) in the internal adapter,
query decomposition / rewriting other than HyDE and multi-hop follow-ups, late-interaction (ColBERT) or
LLM-based reranking, self-reflective / corrective RAG loops (beyond MCP agentic tool use), context compression /
selection under a token budget, fine-tuned or trained retrievers, long-context vs RAG trade-offs,
hallucination-specific metrics beyond RAGAS faithfulness.

## Caveat: `full-grid-example.yaml`
The upstream example still lists `sentence` and `fixed` (not in `chunking.py`) and unprefixed
`sentence-transformers/…` IDs for embedders/rerankers (would resolve to Ollama). Use only the values in the table above.
