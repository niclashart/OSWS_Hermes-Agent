# When Is Additional Retrieval Worthwhile? A Cost-Aware Study of Evidence Gain and Answer Reliability in RAG (arxiv-2610.37358)

**Core idea:** A cost-aware two-action retrieval policy decides per question between dense-retrieval-plus-reranking and hybrid lexical-dense retrieval, using a regularized linear model trained on pre-routing features and frozen before held-out evaluation.

**Key result (verbatim):** "the policy triggers hybrid retrieval on 46 questions (24.5%) and obtains the same evidence Hit@10 as always-hybrid retrieval (78.70%, versus 76.92% for always-keep)" (Abstract)

**Rubric:** A=2 B=1 C=1 D=2 E=1 → 7/10. Retrieval routing touches the Retrieval axis; single dataset (QASPER subset) and authors flag weak statistical power; 4-bit Qwen3-4B runs on consumer GPU; hybrid/routing needs a new component.

**Affected axis:** Retrieval
