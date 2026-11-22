# LSP-RAG: Latent Scoring Perspectives for Knowledge Graph Retrieval-Augmented Generation

arXiv 2611.25229 · screened 2026-11-22 · score 7/10 (A2 B2 C1 D2 E0)

## Core idea
KG-RAG with multi-hop triplet retrieval driven by a lightweight, trained scoring module instead of an LLM in the retrieval loop. K latent scoring perspectives, each parameterized by a learnable *perspective-specific soft prompt*, score candidate triplets; a *contextual soft prompt* updated per hop encodes query + previously explored triplets. Perspective scores are adaptively aggregated per (question, triplet) pair. Backbone LMs stay frozen; only soft prompts, projection and aggregation layers are trained with a contrastive (cross-entropy) loss over gold vs. distractor triplets.

## Key results (verbatim quotes)
- Abstract: "LSP-RAG achieves superior performance across multiple KG-based Question Answering benchmarks compared to existing retrieval systems, including those that rely on much larger language models, demonstrating its effectiveness under limited computational budgets."
- §IV-G: "LSP-RAG demonstrates strong performance even under lightweight language models, outperforming ToG/RoG even when using ChatGPT as its retriever."
- Table I: accuracy with Flan-T5-3B retriever — WebQSP 88.59 (vs. ToG 72.25), WikiMovies 98.22, MetaQA-1hop 96.84, MetaQA-2hop 94.95.
- §IV-I: "removing either consistently degrades performance" (perspective-specific and contextual soft prompts; e.g. WebQSP Flan-T5 88.59 → 86.23 w/o contextual).

## Rubric justification
- A=2: graph RAG + trained retriever — new technique, no NIMBF axis.
- B=2: 4 KGQA datasets, broad baselines (ToG, RoG, GNN-RAG, G-Retriever, Sim-Retrieve), ablations, 5 seeds.
- C=1: no code/weights link found in paper.
- D=2: lightweight backbones (Flan-T5-3B, LLaMA3-8B); training used 4×A100 but scoring heads are tiny.
- E=0: needs a KG store, hop-wise candidate expansion and a trained scorer — framework redesign for RAG-NIMBF.

## Affected axis
New-Techniques (Graph RAG / trained retriever — both in `nimbf-capabilities.md` "not expressible today").
