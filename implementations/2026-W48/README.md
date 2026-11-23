# Implementation check 2026-W48

| id | title | NIMBF | Blueprint | proposed | reason |
|---|---|---|---|---|---|
| arxiv-2611.22392 | Deal With It: Better Schedules for Listwise Reranking | missing | not-applicable | yes (NIMBF) | LLM listwise reranking absent; dealing schedule cuts repair calls 59%→14% |
| arxiv-2611.25071 | FinVeriQA: Financial Research Agents | missing | partial | yes (both) | Independent-evidence verification absent in NIMBF; Blueprint check reuses shared evidence |
| arxiv-2611.22509 | MIPR multimodal intent-to-product benchmark | partial | not-applicable | no | Multimodal dataset adapter needed; text-only slice already expressible via hf-generic — low marginal value |
| hf-f4roukb_denserepr-code-48M-pretrain-EN-v1 | denserepr-code 48M embedder | exists | not-applicable | no | Plugs into existing `embedding_models` slot (`huggingface:…`) via config.yaml — weekly fit check territory, no code needed |
| hf-OpenMed_EmbeddingGemma2-BiomedicalEvidence-270M-v2 | OpenMed biomedical embedder | exists | not-applicable | no | Existing slot; weak evidence (own unverified numbers, no external baselines) |
