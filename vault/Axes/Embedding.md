---
tags: [rag-radar, axis]
---
# Embedding

Back to [[RAG Radar]] · capabilities: see `reference/nimbf-capabilities.md`

## Papers
- [[arxiv-2610.30705]] — ULME: unified embedder+generator checkpoints, +3.3-4.1 MTEB (7)
- [[2610.32122]] — Shows sentiment is linearly decodable from modern embedder outputs (up to 91.3%) (7)
- [[2610.40122]] — xPRT: Cross-Passage Retrieval Pretraining (7)
- [[2610.38854]] — Contextual embeddings beyond the gold chunk: multi-chunk + evidence relevance (8)
- [[hf-VAGOsolutions_SauerkrautLM-MoEdernColBERT-27M]] — 27M multilingual ColBERT, beats Qwen3-0.6B on German MKQA (8)
- [[hf-VAGOsolutions_SauerkrautLM-MoEdernColBERT-115M]] — 115M MoE ColBERT, MKQA de→en 0.731, LongEmbed 90.1 (8)
- [[hf-nlpai-lab_KURE-v3]] — Korean dense retriever 1.1B, 0.8027 MTEB(kor) above 8B models (9)
- [[hf-Yaldat_Yalda-Embedding]] — Persian fine-tune of Qwen3-Embedding-0.6B, FaMTEB mean 0.5488 vs 0.4713 base (7)
- [[hf-opensearch-project_opensearch-neural-embed-v1]] — 598M distilled embedder, BEIR #1 <1B (58.37 NDCG@10) (10)
- [[hf-f4roukb_denserepr-code-48M-pretrain-EN-v1]] — 48M code-retrieval embedder, 64.84 nDCG@10 CoIR, best dense (10)
- [[arxiv-2611.19862]] — 43M-param biomedical embedder (RetroMAE pretraining) beats BERT-base bi-encoders (8)
- [[hf-OpenMed_EmbeddingGemma2-BiomedicalEvidence-270M-v2]] — 271M biomedical fine-tune of embeddinggemma-2, MedQuAD NDCG@10 91.76, no external baselines (8)
- [[hf-harims95_hobbylm-embed-140m]] — 140M sparse-MoE embedder, MTEB(eng,v2) 62.33, Apache-2.0, slot-ready (7)
- [[hf-dotproductx_breadbowl-embed-v1.3]] — 0.8B slot model, embed+rerank in one pass, 50x faster rerank, Apache-2.0, new provider needed (8)
- [[hf-FrontiersMind_EmbeddingNandi-150M]] — 146M embedder, 16K context, En+Indic, MTEB avg 71.99 vs granite 50.97, Apache-2.0, slot-ready (8)
