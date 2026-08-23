# Lab 15 — Build a Clean-to-Risk Pipeline with pipe

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO7
- Tools: Pandas, CSV, unittest

## Scenario

A credit-risk team wants the DataFrame transformations to read like an auditable sequence rather than one large notebook cell.

## Goal

A chain of named clean, enrich, score and summarise functions connected with pipe().

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 15 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- `loan_pipeline.csv`

## Step-by-step

1. Load loan_pipeline.csv and preserve a raw copy for comparison.
2. Write clean_data(df) without mutating its input.
3. Write add_features(df) for affordability and utilisation ratios.
4. Write score_risk(df) using vectorised conditions or apply.

   ```bash
   python starter.py
   ```
5. Chain the functions with pipe and export results.

   ```bash
   python solution.py
   ```
6. Run tests for immutability, boundaries and row counts.

   ```bash
   python -m unittest test_solution.py
   ```

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

Each stage can be tested alone, the raw DataFrame is unchanged, and the final risk-band counts reconcile to total rows.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
