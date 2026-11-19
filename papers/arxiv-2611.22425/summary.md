# LMMR: Learned Multigranular Memory Retrieval for Small Language Model Agents (2611.22425)

Score: 7/10 (A 2, B 2, C 1, D 1, E 1)

## Core idea
Learned multigranular memory retrieval selects source + read length under a token budget.

## Key result (verbatim)
> "On 22,398 official validation questions from HotpotQA, 2WikiMultihopQA, and MuSiQue, a frozen 2B answer model reaches 61.47, 43.26, and 30.58 F1 under a 400-token budget." (Abstract)

## Rubric justification
learned budgeted evidence selection = new technique; 3 datasets + significance; training required (C=1, E=1); 2B models feasible (D=1)

## Affected axis
Retrieval: Not expressible: learned selection beyond similarity/MMR/multi-hop. Weekly fit check -> new-axis.md.
