# f4roukb/denserepr-code-48M-pretrain-EN-v1 — summary

Score: 10/10 · Type: HF embedder (code retrieval) · License: apache-2.0

## Core idea
Continued contrastive pretraining of `ibm-granite/granite-embedding-small-english-r2` on ~23M code
retrieval pairs (in-batch negatives only) yields a 48M-param dense code-retrieval embedder:
384-d vectors, CLS pooling, 8,192-token context, ModernBERT architecture, no prompts needed.

## Key results (verbatim quotes from the model card)
- "It scores **64.84 mean nDCG@10 on CoIR** (10 tasks), +11.4 over the model it was trained from."
- "Among the dense (single-vector) models on the MTEB CoIR leaderboard with all 10 tasks, it is the best one"
  (truncated in card; measured with `mteb` 2.27.8, bf16)
- Per-task vs base (nDCG@10 ×100): CodeFeedbackMT 52.20 → 81.19, COIRCodeSearchNetRetrieval 60.42 → 79.90,
  SyntheticText2SQL 46.44 → 59.69; only CosQA regresses slightly (35.40 → 33.84).
- Stage caveat (card): "This is the **pretraining stage**: no hard negatives, no distillation and no
  fine-tuning stage have been applied yet."

## Rubric
A 2 · B 2 · C 2 · D 2 · E 2 — A: best dense single-vector model on MTEB CoIR, a clear new capability
(code retrieval) at 48M params; B: standardized MTEB CoIR numbers with the base model as baseline;
C: apache-2.0, sentence-transformers weights; D: 48M params, trivially consumer-GPU/CPU;
E: `SentenceTransformer`-loadable, plugs directly into the embedding axis.

## RAG-NIMBF relevance
Ready-to-use slot line:
`embedding_models: huggingface:f4roukb/denserepr-code-48M-pretrain-EN-v1`
Natural experiment: compare against the current default embedder on a code/QA dataset (one axis changed).
English/code only — not a drop-in for multilingual corpora.

## Links
- Model card: https://huggingface.co/f4roukb/denserepr-code-48M-pretrain-EN-v1
- Base model: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2
