# Scan or Index? Evidence Coverage, Answer Quality, and Cost in Long-Document RAG (arXiv:2610.28957)

## Core idea
Compares 11 retrieval configurations (lexical, dense, hybrid reranking, full-document scanning with Jev / OpenAI Decisions / Cloudflare Clef) on 396 QASPER questions and 80 textbook questions with a fixed generator and five-passage limit.

## Results
> "On books, Hybrid + Jev achieves the highest observed evidence coverage (94.1%), compared with 88.7% for Jev full scan and 81.3% for OpenAI dense retrieval" (Abstract). And: "Hybrid + Decisions achieves the highest observed book Answer Accuracy among retrieval methods (0.892), despite recovering less reference evidence" — higher coverage does not consistently yield better answers; full scanning incurs much higher latency/cost (e.g. books ≥ $0.064/query vs dense 3.8e-7, Appendix B). CC BY 4.0.

## Rubric
A 2 · B 2 · C 2 · D 2 · E 0 — new retrieval-mode comparison (scan vs index); 2 corpora, controlled setup; open license; runnable; RAG-NIMBF has no scan-mode slot.

## Relevance for RAG-NIMBF
Candidate new value for `settings.retrieval_mode` (e.g. `full-scan`) or new long-document axis; evidence-coverage metric for Evaluation axis.
