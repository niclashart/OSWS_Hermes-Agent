# MEMORA: Memory-Enhanced Multimodal Committee Reranking Agent (arXiv:2610.25282)

## Core idea
Agentic reranking for reasoning-intensive (multimodal) retrieval: (1) Collaborative Factor-Committee Reranking decomposes queries into intent factors, extracts factor-specific evidence, and synthesises a meta-verdict; (2) an Episodic Memory Module adjusts priorities across queries at inference time; (3) a Reasoning-Aware Dense Retriever fine-tuned with chain-of-thought augmentation.

## Results
> "MEMORA achieves nDCG@10 of 41.5 (text-to-text) and 38.9 (multimodal query-to-text), outperforming the strongest agentic text-only baseline by +8.3 points and the strongest agentic multimodal baseline by +7.9 points" (Abstract; MM-BRIGHT, 29 domains). Code: https://github.com/HarnessLab/MEMORA.

## Rubric
A 2 · B 2 · C 2 · D 2 · E 0 — agentic committee reranking with memory + fine-tuned retriever; single benchmark but strong baselines and ablations (pool-size, failure modes); open code; not expressible in NIMBF.

## Relevance for RAG-NIMBF
New-Techniques: query decomposition + memory-conditioned reranking both outside current axes.
