# Modular and Efficient Approximate Nearest Neighbors Search with Vectorium and kANNolo

- arXiv: https://arxiv.org/abs/2611.03927
- Screened: 2026-11-04 · Score: 8/10 · Rubric A-E: (1, 2, 2, 2, 1)
- Axis: Vector-Store

## Core idea
Two open-source Rust ANN libraries that factor vector representation, distance, quantizer and index independently; HNSW/IVF indexes generic over dense/sparse/multi-vector, matching or beating Faiss on memory-throughput trade-offs.

## Key results (verbatim quotes)
> "our Product Quantization matches Faiss in accuracy at competitive speed, our RaBitQ and HNSW match or outperform their reference implementations, and our IVF outperforms Faiss." (Abstract)

## Rubric justification
A=1: ANN index layer sits under the Vector-Store axis; B=2 six dense + five sparse systems on seven collections; C=2 open-source Rust; D=2 CPU-only; E=1 would need a new vector_db_backend adapter.

## RAG-NIMBF relevance
Maps to the **Vector-Store** axis; see vault note.
