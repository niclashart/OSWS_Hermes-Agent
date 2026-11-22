# Retrieving Patristic References and Modelling Topics in Bullinger's Reformation Correspondence

arXiv 2611.25247 · screened 2026-11-22 · score 7/10 (A2 B2 C2 D2 E1)

## Core idea
Humanities IR study comparing lexical (BM25), dense (bi-encoder) and hybrid retrieval for detecting patristic (Church Fathers) references in Bullinger's Latin correspondence. Key finding: BM25 wins on explicit citations, dense retrieval on implicit references; the two recover largely disjoint implicit sets, so rank fusion recovers most of what an expensive cross-encoder would — at a fraction of the inference cost. Also: seed-guided topic modelling (extended FASTopic) gives minimal coherence gains; topics not usable for retrieval.

## Key results (verbatim quotes, abstract)
- "BM25 outperforms dense approaches on explicit citations (94%, R@20)."
- "Because BM25 and dense retrieval recover disjoint sets of implicit references, fusing their rankings raises implicit R@20 to 22%, close to cross-encoder reranking of the same candidates (26%) but without its inference cost."
- "dominant topic weights barely exceed a uniform distribution, making topics unusable to inform retrieval."
- Best bi-encoder (Latin encoder fine-tuned on biblical reuse): "82%, Recall@20 on explicit and 16% on implicit references".

## Rubric justification
- A=2: hybrid BM25 + dense fusion (RRF) is a known gap in RAG-NIMBF's internal adapter (`nimbf-capabilities.md` "not expressible today").
- B=2: real historical corpus, multiple retrievers, explicit vs. implicit reference split, cross-encoder upper bound.
- C=2: CC-BY 4.0 license (arXiv metadata).
- D=2: BM25 + bi-encoders run on CPU/small GPU.
- E=1: hybrid fusion needs a new component in the internal retrieval adapter; embedders themselves are plug-in.

## Affected axis
New-Techniques (hybrid BM25+dense fusion in internal adapter) — evidence for a fusion axis value.
