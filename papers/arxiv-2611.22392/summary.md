# Deal With It: On Better Schedules for Listwise Reranking (2611.22392)

Score: 9/10 (A 2, B 2, C 2, D 2, E 1)

## Core idea
Round-robin dealing of candidates cuts repair calls in listwise LLM reranking schedules.

## Key result (verbatim)
> "In existing schedules such as BlitzRank, dealing reduces repair calls from 59% of queries to 14%, improving latency with no significant change in quality." (Abstract)

## Rubric justification
LLM listwise reranking schedule = new provider in Reranking axis; strong theory + 6-LLM experiments; open code (C=2); API-based (D=2); schedule plug-in (E=1)

## Affected axis
Reranking: Reranking axis only supports cross-encoder reranker_models; LLM listwise schedules = new provider. Weekly fit check -> new-axis.md.
