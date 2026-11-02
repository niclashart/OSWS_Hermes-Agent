# ProSearch: Benchmarking Multi-Constraint Protocol Retrieval in Experimental Science

arXiv 2610.41396 · Score 9/10 · Axis: Datasets

## Core idea
A benchmark for retrieval of experimental-science protocols under 3–5 interdependent explicit constraints (incl. numerical and negation constraints), built from real experimental records with evidence-based relevance validation. 1,515 queries, six domains, 60 experimental fields with dependencies.

## Results
> "The best-performing retriever achieves an average nDCG@10 of only 0.290, which improves to 0.474 with reranking." (Abstract / Sec. 6)
> "We find that reranking improves this score to 0.474, while query reformulation yields only modest gains." (Sec. 6)
> "manual error analysis identifies joint constraint binding as a key bottleneck" (Abstract)

## Rubric
A 2 (new retrieval benchmark → Datasets axis) · B 2 (19 retrievers, structured diagnostics) · C 2 (code/benchmark released) · D 1 (benchmark evaluation is API/LLM-cost bound, retrievers themselves small) · E 2 (loadable as `hf-generic`/`jsonl` dataset via fields; no framework change)

## Relevance for RAG-NIMBF
New dataset option on the `Datasets` axis: `dataset.name: hf-generic` with `dataset_question_field` / `dataset_ground_truth_field` / `dataset_context_field`, `custom_retrieval_metrics_mode: gold_doc` for nDCG@10. Multi-constraint filtering itself is a new technique (constraint-aware ranking not expressible).

## Status log
- 2026-11-02 screened
