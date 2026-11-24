# Detecting Word-Substitution Poisoning of a RAG Knowledge Base with Relative Entropy and Runtime Verification

arXiv: 2611.27410 · Screened: 2026-11-24 · Score: 8/10

## Core idea
Studies a stealth attacker that edits existing RAG corpus passages by synonym substitution (PWWS, TextFooler) in a cybersecurity RAG (MITRE ATT&CK/CAPEC). Detection via the log-ratio term of relative entropy between a word and its most probable synonym under a small LM (AUROC 0.95); used as a retrieval filter plus a runtime monitor checking answers against trusted STIX data, remembering rejected passages.

## Key results
> "poisoning lowers judged answer correctness from 0.714 to 0.555" (Abstract)
> "with a small language model as the reference, it reaches an AUROC of 0.95 and stays near chance on the control" (Abstract)
> "it reduces exposure to edited text from 0.41 to 0.26; when it may add the trusted MITRE entry as a source, correctness rises to 0.786." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 0
A=2: corpus poisoning detection + guardrail/runtime verification — new security technique for RAG pipelines; B=2: 44-question reviewed benchmark, paired runs, control corpus, per-defence costs and failure cases; C=1: code availability not stated in abstract; D=2: small LM reference model, consumer-GPU feasible; E=0: RAG-NIMBF has no poisoning / robustness / guardrail axis — needs new component and metric.

## Affected axis
New-Techniques (RAG robustness / poisoning detection / guardrails)

## Status log
- 2026-11-24 screened (score 8)
