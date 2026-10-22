# EpiLens: Lightweight RAG for Epidemiological Knowledge Acquisition (arXiv:2610.26730)

## Core idea
Open-source RAG package applying a fixed retrieval template and output schema to every paper in a corpus, linking outputs to source passages. Corpus of 2,297 epidemiology papers; paper-classification workflow evaluated against 214 manually labelled papers without task-specific training.

## Results
> "the classifier matches or exceeds the tested supervised and zero-shot baselines across four tasks" (Abstract). E.g. model-based share for reproduction-number vs fatality-risk papers: "54% versus 22%, compared with 62% versus 24% in the manual labels" (Abstract). Open source.

## Rubric
A 2 · B 2 · C 2 · D 2 · E 0 — applied RAG with fixed-template schema extraction pattern; human-labelled evaluation; open source; lightweight; domain workflow not an axis value.

## Relevance for RAG-NIMBF
Pattern (fixed template + output schema + source passage linking) maps loosely to Prompting/Evaluation, but as a package it is a RAG-System adapter candidate, not a config value.
