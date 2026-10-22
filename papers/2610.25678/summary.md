# Cross-Pollination Retrieval (CPR-Dataset) (arXiv:2610.25678)

## Core idea
Cross-pollination retrieval: finding papers across research fields whose ideas transfer. CPR-Dataset mined from cross-topic citations; CPR-eval (1,300 queries, 26 fields), CPR-train (10,573 pairs). Shows existing retrievers nearly fail this task; contrastive fine-tuning on CPR-train transfers to AnaloBench and BRIGHT.

## Results
> "On CPR-eval, the best of eleven existing retrievers reaches a Recall@10 of only 0.26, whereas an LLM reranker reaches 0.81. Standard contrastive fine-tuning on CPR-train raises Recall@10 to as high as 0.70" (Abstract). "On BRIGHT, it raises nDCG@10 by up to 70%" (Abstract). HF: huggingface.co/CPR-Dataset, code: github.com/SeokwonJung-Jay/Cross-Pollination-Retrieval.

## Rubric
A 2 · B 2 · C 2 · D 2 · E 0 — new retrieval task + dataset + fine-tuned retriever; multi-benchmark transfer; open data/code; fine-tuned retrievers are explicitly not expressible in NIMBF.

## Relevance for RAG-NIMBF
Candidate dataset adapter (CPR-eval) for Datasets axis; fine-tuned retriever support would need a new Embedding/Retrieval capability.
