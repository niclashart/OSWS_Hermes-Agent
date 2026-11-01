# nvidia/Nemotron-3.5-Rerank-8B-BF16 — model summary

- **Type:** HF reranker (cross-encoder, text + page-image multimodal), 8.4B params, license OpenMDW-1.1
- **Slot:** `reranker_models: huggingface:nvidia/Nemotron-3.5-Rerank-8B-BF16`
- **mteb:** https://github.com/embeddings-benchmark/results/tree/main/results/nvidia__Nemotron-3.5-Rerank-8B-BF16

## Core idea
NVIDIA cross-encoder reranker for multilingual and multimodal QA retrieval: scores a text query against documents that may be text, page images, or both (charts, tables, infographics). Base: Ministral-3-8B-Instruct. Evaluated on text retrieval across 34 languages (incl. German) and image retrieval across 18 languages. Targets classical and agentic vision RAG pipelines.

## Reported results (quotes from model card)
- "Nemotron-3.5-Rerank-8B-BF16 achieves state-of-the-art results on the new ViDoRe v3.1 Reranking leaderboard as of October 20, 2026."
- "The model can be integrated into classical or agentic vision RAG pipelines."
- "For text retrieval, the model was evaluated across 34 languages: English, Arabic, … German, …"
MTEB results link present.

## Rubric
A 2 — SOTA on ViDoRe v3.1 reranking; beats current reranker options; adds multimodal (page-image) reranking capability.
B 2 — public leaderboard (ViDoRe v3.1) + MTEB results link.
C 1 — OpenMDW-1.1 is permissive and commercial-ready but not MIT/Apache/CC-BY.
D 2 — 8B BF16 ≈ 16 GB, fits a 24 GB GPU.
E 1 — multimodal reranker with custom logit output; not a plain sentence-transformers `CrossEncoder` → new provider.

## Affected axis
Reranking (multimodal variant — not expressible today; new-axis candidate).
