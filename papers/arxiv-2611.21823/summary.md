# TUSI: A Citation-Grounded Graph-Based Benchmark (2611.21823)

Score: 8/10 (A 1, B 2, C 2, D 2, E 1)

## Core idea
Persian legal RAG benchmark with citation grounding + graph retrieval (+8pp recall).

## Key result (verbatim)
> "Experimental results demonstrate that incorporating graph-based relations improves retrieval recall by up to 8 percentage points compared to standard baselines." (Abstract)

## Rubric justification
new domain RAG dataset (Persian legal); recall eval + MC QA; open data; consumer-GPU feasible; dataset adapter needed (E=1)

## Affected axis
Datasets: Datasets axis: hf-generic adapter may load TUSI-QA if fields map (dataset_question_field etc.); graph-retrieval baseline itself not expressible.
