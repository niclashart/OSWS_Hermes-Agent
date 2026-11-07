# From Logs to Faults: Reference-Free Fault Localization for RAG Pipelines (arXiv-2611.03725)

**Core idea.** RAGLog: detects and localizes faults per RAG stage (rewriter, embedder, retriever, reranker, generator) from execution logs — no reference answers, no instrumentation. Transforms API logs into a common RAG schema, runs rule-based + embedding-based + LLM-based stage checks, and an ensemble classifier decides the faulty stage. Ships as an open-source tool with a 3,134-run labeled fault dataset.

**Key results.**
> "With Claude Haiku 5.5, RAGLog achieves a pooled F1 score of 0.73 on runs with naturally occurring faults, outperforming Claude Code (0.58) and Codex (0.52), and comparable effectiveness on runs with injected faults (0.84 versus 0.80 and 0.82, respectively)." (Abstract)
> "It analyzes runs in approximately five seconds at US$0.005 each, with overall lower cost and latency than agent baselines." (Abstract)
> "Among the 551 naturally faulty runs in our test set, 202 (37%) still produced correct answers" (Sec. 8.1) — answer-level evaluation misses these.

**Rubric.** A 2 (new evaluation/debugging capability: stage-level fault localization — new benchmarking dimension) · B 2 (5 pipelines, 3,134 labeled runs, agent baselines, ablations; evidence-flow check ablation) · C 2 (open-source tool + labeled dataset released) · D 2 (~$0.005/run via API; rule+embedding checks run locally) · E 1 (new evaluation component: fault-localization metrics over per-stage logs; needs an adapter, not just a config value) = **9/10, relevant**.

**Affected axis:** Evaluation (stage-level fault localization / diagnostics beyond end-answer metrics).

**Source:** https://arxiv.org/abs/2611.03725
