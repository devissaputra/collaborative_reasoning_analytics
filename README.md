# Collaborative Reasoning Analytics

This dialogue-analysis prototype combines transparent move labels, adjacent-turn lexical overlap, and speaker-participation balance on synthetic conversations. Its measures help inspect a coding workflow, but shared words do not prove conceptual uptake and balanced turn counts do not prove equitable reasoning. The repository presents these quantities as descriptive proxies awaiting human annotation and validation.

## Start here

- [Calculations, evidence and verification scope](CALCULATIONS.md)
- [Figure sources and exact numerical paths](docs/figure_spec.json)
- [Data status](data/README.md)

![Study question, data, design and interpretation](assets/review_overview.svg)

![Defined calculation and source-linked evidence](assets/review_calculations.svg)

**Review scope:** The existing suite requires unavailable dependencies; no full-suite pass is claimed. The bundled demonstration executed successfully in this review.

## Detailed project documentation

[![CI](https://github.com/devissaputra/collaborative_reasoning_analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/devissaputra/collaborative_reasoning_analytics/actions/workflows/ci.yml)

**Category:** AI in Education  
**Lightweight NLP for adjacent-turn uptake, participation balance, and transparent reasoning-move summaries in group dialogue.**

> Research prototype. All bundled data and results are synthetic demonstrations. Nothing in this repository should be interpreted as evidence about real learners, teachers, or institutions.


## Why this project exists

Collaboration quality is not captured by who spoke most. This repository separates several inspectable signals: lexical uptake between adjacent turns, participation balance, and transparent reasoning-move categories such as evidence requests and challenges.

The current implementation is deliberately descriptive. It does **not** model dialogue sequences, long-range dependencies, or causal effects between conversational moves.

## Research questions

1. How much lexical uptake occurs across adjacent turns?
2. Is participation distributed or dominated by one speaker?
3. Which transparent reasoning-move categories appear most often in the dialogue?

## What the repository does


The implemented pipeline follows five stages:

1. **Dialogue transcript**
2. **Rule-based reasoning-move tagging**
3. **Adjacent-turn lexical uptake**
4. **Participation balance**
5. **Descriptive conversation report**

The baseline is deliberately transparent so these rule-based measures can later be compared with embedding-based or supervised discourse models.

## Core outputs

- `mean_uptake`
- `participation_balance`
- `reasoning_move_rate`
- `evidence_request_rate`
- `challenge_rate`


The dashboard is generated from **synthetic data** and is included only to demonstrate the analysis surface. It does not report sequence effects or empirical learner outcomes.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .[dev]
python examples/demo.py
pytest -q
```

You can also use Docker:

```bash
docker build -t collaborative_reasoning_analytics .
docker run --rm collaborative_reasoning_analytics
```

## Repository structure

```text
collaborative_reasoning_analytics/
├── src/collaborative_reasoning_analytics/  # core implementation and synthetic-data generator
├── examples/demo.py                        # end-to-end reproducible demo
├── tests/                                  # executable unit tests
├── docs/                                   # research design, data dictionary, references
│   └── images/                             # auditable project diagrams
├── results/                                # synthetic demo outputs only
├── config/default.yaml
├── Dockerfile
├── Makefile
└── pyproject.toml
```

## Research design in one picture


The fuller design rationale is in [`docs/research_design.md`](docs/research_design.md), including constructs, assumptions, validation steps, and a proposed empirical extension.

## Reproducibility choices

- Synthetic generation uses a fixed random seed.
- The core metrics are implemented as small, testable functions.
- The demo writes machine-readable results into `results/`.
- CI runs the tests on every push and pull request.
- No API keys, proprietary datasets, or external model calls are required for the baseline.

## Responsible-use boundaries

- Lexical overlap is only a rough proxy for conceptual uptake.
- Rule-based move labels are transparent baselines, not validated discourse annotations.
- Conversation metrics should support reflection, not rank individual students.
- The current baseline does not implement sequence analysis.

## Strong next experiments

- Fine-tune a discourse-move classifier with inter-rater reliability reporting.
- Add embedding-based uptake and delayed cross-turn references.
- Add explicit sequence models only with a clearly defined temporal research question.
- Visualize group-level reasoning networks over time.

## References

See [`docs/references.md`](docs/references.md). The references locate the project in current AIED, learning-analytics, human-centered AI, and instructional-design research. They do **not** imply endorsement or affiliation.

## Citation

If you build on this research prototype, use the metadata in [`CITATION.cff`](CITATION.cff).

## License

MIT for the code in this repository. Research data from future studies should use a separate data-governance and consent process.
