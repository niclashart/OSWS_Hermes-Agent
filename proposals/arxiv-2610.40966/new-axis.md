# New-axis proposal — arXiv:2610.40966

**Paper:** "Better Retrievers, Worse Labels: How Incomplete Relevance Judgments Distort Abstention Evaluation in Conversational RAG" (arXiv:2610.40966) — vault note [[arxiv-2610.40966]], screened 2026-11-02, score 9/10.

## What the paper shows
Conversational-RAG benchmarks score abstention by reading sufficiency off relevance judgments ("no gold document → unanswerable"). As retrievers improve, this shortcut breaks: better retrieval finds answers in contexts without gold documents. Quote (Abstract / Sec. 4): "The stronger the retriever, the larger the share of no-gold contexts that still contain the answer (28% to 72%) and the lower the shortcut's precision (.68 to .10; .70 to .21 under the audit)." On MTRAG, "precision drops from .72 to .50", and "answerability AUROC is up to .19 too low". Code, runs and labels are released.

## Why not expressible in RAG-NIMBF today
RAG-NIMBF's abstention-related evaluation (`eval_critic_*`, refusal detection custom metric, `custom_retrieval_metrics_mode: gold_doc`) judges refusal against gold-document presence. The paper shows this label source is systematically wrong for strong retrievers. What is missing:

1. **Content-sufficiency labels** — an answerability signal derived from whether the retrieved context actually contains the answer (LLM judge or sufficiency detector over the context), independent of gold-document IDs. RAG-NIMBF's gold-doc metrics cannot represent this.
2. **A shortcut-audit metric** — reporting abstention-metric precision/AUROC under both label regimes (gold-presence vs. content sufficiency), so the label shortcut becomes visible in benchmark output.
3. **A retrieval-score detector arm** — the paper found "the best sufficiency detector appears to be a retrieval score that never reads the documents"; comparing judge-based vs. retrieval-score abstention gates is not expressible.

## What RAG-NIMBF would need
- New config keys (settings):
  - `abstention_label_mode: <gold_doc | content_sufficiency | both>`
  - `sufficiency_judge: <model id>` (LLM judge over retrieved context) and `sufficiency_gate_source: <judge | retrieval_score>`
- New component: a sufficiency-labeling step in `benchmark/evaluation.py` that produces per-query answerability labels from the retrieved context before scoring refusal/abstention.
- New custom metrics: abstention precision and answerability AUROC computed against the chosen label mode, reported side by side when mode is `both`.

## Estimated effort
Medium (~1 week): the critic/LLM-judge infrastructure exists (`eval_critic_*`, RAGAS); the work is a new label producer, the two metrics, and config wiring plus tests. No framework redesign — it composes with the existing Evaluation axis.
