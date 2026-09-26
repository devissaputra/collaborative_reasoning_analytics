# Calculation guide

## Question and evidence

How can dialogue participation and uptake be inspected?

Synthetic ordered dialogue turns and speaker identities.

**Status:** SYNTHETIC / RULE-BASED PROTOTYPE | no educational validity claim.

## Design

Lexical move rules; adjacent-turn token overlap; normalized speaker entropy.

## Calculation and interpretation

`Uptake proxy = |tokens(previous) ∩ tokens(current)| / |union|.`

This is lexical overlap, not semantic understanding. Participation entropy is normalized by the number of observed speakers. Turn order must belong to one conversation; mixing conversations would create invalid adjacency.

## Evidence table

Selected recorded values (units and context shown). Full precision below is for traceability, not a claim of measurement precision.

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| mean_uptake | 0.231 | unitless | `mean_uptake` |
| participation_balance | 0.995 | unitless | `participation_balance` |
| reasoning_move_rate | 0.172 | unitless | `reasoning_move_rate` |
| evidence_request_rate | 0.45 | unitless | `evidence_request_rate` |
| challenge_rate | 0.183 | unitless | `challenge_rate` |

Source: [results/demo_metrics.json](results/demo_metrics.json). Values resolve directly from this file when figures are regenerated.

This dialogue-analysis prototype combines transparent move labels, adjacent-turn lexical overlap, and speaker-participation balance on synthetic conversations. Its measures help inspect a coding workflow, but shared words do not prove conceptual uptake and balanced turn counts do not prove equitable reasoning. The repository presents these quantities as descriptive proxies awaiting human annotation and validation.

## Verification performed in this review

The existing suite requires unavailable dependencies; no full-suite pass is claimed. The bundled demonstration executed successfully in this review.

The figure-generation check verifies agreement between the selected source values and SVGs. It does not validate the raw dataset, fitted model, identification assumptions, or external generalization.

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

## Implementation map

Follow these functions to inspect each transformation. Validation helpers and private functions remain visible in the linked modules.

| Function | Purpose / documented behavior |
|---|---|
| [`main`](src/collaborative_reasoning_analytics/cli.py#L5) | Inspect the explicit implementation and its callers. |
| [`tokens`](src/collaborative_reasoning_analytics/core.py#L8) | Inspect the explicit implementation and its callers. |
| [`semantic_uptake`](src/collaborative_reasoning_analytics/core.py#L9) | Inspect the explicit implementation and its callers. |
| [`classify_move`](src/collaborative_reasoning_analytics/core.py#L11) | Inspect the explicit implementation and its callers. |
| [`participation_balance`](src/collaborative_reasoning_analytics/core.py#L18) | Inspect the explicit implementation and its callers. |
| [`conversation_metrics`](src/collaborative_reasoning_analytics/core.py#L22) | Inspect the explicit implementation and its callers. |
| [`make_dialogue`](src/collaborative_reasoning_analytics/synthetic.py#L3) | Inspect the explicit implementation and its callers. |

## What remains before a stronger research claim

This is lexical overlap, not semantic understanding. Participation entropy is normalized by the number of observed speakers. Turn order must belong to one conversation; mixing conversations would create invalid adjacency. A successful software test is not validation of a scientific construct. New experiments should state their split unit, comparator, outcome, uncertainty procedure and failure criteria before examining final test results.
