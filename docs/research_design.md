# Research design

## Project aim

Collaboration quality is not captured by who spoke most. This repo focuses on whether participants build on one another’s ideas, ask for evidence, challenge claims, and connect reasons to conclusions.

## Research questions

1. How much semantic uptake occurs across adjacent turns?
2. Is participation distributed or dominated by one speaker?
3. Which reasoning moves appear, and how are they sequenced?

## Baseline analytic pipeline

1. Dialogue transcript
2. Reasoning move tagging
3. Semantic uptake
4. Participation balance
5. Conversation report

## Construct-to-measure discipline

The repository intentionally distinguishes **constructs** from **proxies**. A behavioral feature may be consistent with a construct without proving that construct exists. A real study should establish content validity, reliability, sensitivity to context, and convergent/discriminant evidence before attaching strong interpretations.

## Minimum empirical extension

1. Pre-register the main research question and analysis plan.
2. Recruit a context-appropriate sample with consent and a documented data-governance plan.
3. Establish annotation reliability or measurement reliability before model comparison.
4. Split exploratory analysis from confirmatory evaluation.
5. Report uncertainty, subgroup performance, missing-data patterns, and negative findings.
6. Evaluate whether the output is understandable and useful to the people expected to act on it.

## Threats to validity

- Lexical overlap is only a rough proxy for conceptual uptake.
- Rule-based move labels are transparent baselines, not validated discourse annotations.
- Conversation metrics should support reflection, not rank individual students.

## Next experiments

- Fine-tune a discourse-move classifier with inter-rater reliability reporting.
- Add embedding-based uptake and delayed cross-turn references.
- Visualize group-level reasoning networks over time.
