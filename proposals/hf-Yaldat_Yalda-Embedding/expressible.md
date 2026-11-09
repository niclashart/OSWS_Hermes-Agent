# New-axis proposal — hf-Yaldat/Yalda-Embedding → EXPRESSIBLE

**Model:** Yaldat/Yalda-Embedding — vault note [[hf-Yaldat_Yalda-Embedding]], screened 2026-11-09, score 7/10, E = 2.

## Decision
**Expressible** — the model is a sentence-transformers loadable dense embedder (fine-tune of Qwen3-Embedding-0.6B, Apache 2.0), so it plugs directly into the supported `embedding_models` slot as `huggingface:Yaldat/Yalda-Embedding`. Proposal: `config.yaml` in this directory — one axis changed (baseline `huggingface:Qwen/Qwen3-Embedding-0.6B` vs. variant), Persian retrieval dataset `MCINext/persian-web-document-retrieval` via the `hf-generic` adapter, `custom_retrieval_metrics_mode: gold_doc` for nDCG@10.

Note: HF adapter id (`DATASET_HF_ID`) is env-driven (`DATASET_NAME=hf-generic` reads `DATASET_HF_ID` / `DATASET_*_FIELD` from `.env`, see RAG-NIMBF `benchmark/dataset_adapters.py`, `main@f4b01f6`), so the run needs those env vars set alongside the manifest. Risk: the qrels layout (`query-id`/`corpus-id`/`score`) is a retrieval-pair schema, not a per-row QA schema — if `hf-generic` cannot map it directly, export a flattened JSONL (question / gold corpus-id / context) and switch the dataset name to `jsonl` with `corpus_path`; schema and hypothesis unchanged.
