# RAG Compositionality (LASAGNA) (arXiv:2610.29722)

## Core idea
Controlled study of whether individually strong RAG techniques survive composition. LASAGNA, an open-source evaluation framework, tests 450 configurations across 8 benchmarks and corpora from 5K to 200K documents, with pre-declared hypotheses. Directly methodologically adjacent to RAG-NIMBF's full-grid approach.

## Results
> "three retrieval techniques predict a +47% combined improvement but deliver only +17% when used together" (Abstract). Also: "component gains stack differently for retrieval and faithfulness, and optimizing one can hurt the other", and "the best composition changes as the corpus grows" (Abstract). Appendix F: reranker/embedding inventories with NDCG@10, e.g. ms_marco_minilm_l6 +0.0427 vs no_rerank, bge_reranker_v2_m3 −0.0573. Code: https://github.com/dolev31/lasagna, CC BY 4.0.

## Rubric
A 2 · B 2 · C 2 · D 2 · E 1 — benchmark/methodology directly relevant to NIMBF's axes; strong evidence; open source; consumer-GPU; findings map onto existing axis-combination evaluation.

## Relevance for RAG-NIMBF
Validates full-grid composition testing; corpus size and retrieval-vs-faithfulness metric divergence are evaluation variables RAG-NIMBF should report (Evaluation axis).
