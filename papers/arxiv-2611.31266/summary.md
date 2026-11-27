# Agentic Systems Need Multi-Run Evaluation (arXiv 2611.31266)

## Core idea
Studies run-to-run variability of a deployed agentic RAG system (739 questions × 10 runs). Separates any-run from every-run success, and attributes answer divergence between run pairs to the first pipeline step where the runs differ (routing, retrieval, reasoning, trace depth, generation).

## Key results
> "the retrieval hit rate is 69.4% when the correct page is found in at least one run, but 50.9% when it must be found in all ten." (Abstract) — an 18.5 pp any-run/every-run gap; per-run rate 61.5% (Sec. 3).

> "retrieval is the largest source of divergence (43.9%), and the number of parallel searches at the first retrieval step alone accounts for 20.1% of divergent pairs." (Abstract; Table 1)

> "Responses also stay similar in meaning while varying in wording, with an average BERTScore of 0.90 and a BLEU of 0.49." (Abstract)

> "the agent typically retrieves the ground-truth page within the first two retrieval steps, yet continues searching after the hit in 89.8% of runs." (Appendix C, Table 6)

## Rubric score: 7/10
A 2 — new evaluation protocol (multi-run: any-run/every-run accuracy, BERTScore/BLEU consistency gap, divergence attribution) for the Evaluation axis. B 2 — 7,390 runs of a deployed system, trace-level analysis. C 1 — no code or data release mentioned. D 1 — requires a deployed agentic system + LLM judges; analysis itself is light. E 1 — RAG-NIMBF has no run-repetition axis or run-aggregation metrics; needs new config key + metrics.

## Affected axis
Evaluation (multi-run protocol: run count, any-run/every-run hit rates, cross-run BERTScore/BLEU, divergence attribution); RAG-System (applicable to the `mcp` agentic adapter, where sampling causes variability).

## Relevance for RAG-NIMBF
RAG-NIMBF currently runs each config once. A `benchmark_runs` setting with any-run/every-run aggregation of existing hit@k metrics would make single-run scores comparable against reliability bounds; most valuable for `mcp_execution_mode: agentic`.
