# Make Position Uninformative: Exchangeable Self-Distillation Flattens the Lost-in-the-Middle Curve

arXiv: 2611.28638 · Screened: 2026-11-24 · Score: 8/10

## Core idea
Exchangeable Self-Distillation (ExSD): train a small LoRA adapter on shuffled contexts to reproduce the model's answer when it reads the answer document alone — no gold answers, only a few thousand examples. Removes the lost-in-the-middle U-curve of RAG readers.

## Key results
> "On six models from 1.5B to 32B parameters, ExSD raises both average and worst-position accuracy against the frozen model, including on a held-out test split." (Abstract)
> "In controlled LoRA comparisons, it significantly improves both criteria over Pos2Distill." (Abstract)
> "A single LoRA adapter trained on 2.3k examples of 20-document QA lifts every middle position on Vicuna-7B and on Qwen2.5 from 7B to 32B." (Fig. 1 caption)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 0
A=2: reader-side positional-bias mitigation is a new generation/reader technique for RAG; B=2: six models, LITM protocol, baselines Pos2Distill/CORD/gold fine-tuning, ablations; C=1: code availability not stated in abstract; D=2: LoRA on 1.5–32B models, consumer-GPU feasible for small variants; E=0: requires a training loop (adapter distillation) — RAG-NIMBF has no trained-generator support.

## Affected axis
New-Techniques (positional-robust reader adaptation; long-context vs RAG axis gap)

## Status log
- 2026-11-24 screened (score 8)
