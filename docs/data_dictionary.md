# Data dictionary

The baseline code documents its expected columns directly in `src/collaborative_reasoning_analytics/core.py` and `src/collaborative_reasoning_analytics/synthetic.py`. This keeps the schema close to the executable logic.

## Principles

- Use the minimum data needed for the research question.
- Separate identifiers from analytic features.
- Record provenance for derived variables.
- Treat missingness as information about the measurement process, not merely a nuisance.
- Never convert a research proxy into a high-stakes label without validation.
