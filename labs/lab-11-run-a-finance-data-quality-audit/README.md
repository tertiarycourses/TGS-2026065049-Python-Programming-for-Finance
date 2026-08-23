# Lab 11 — Run a Finance Data-Quality Audit

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO5
- Tools: Pandas, CSV, JSON

## Scenario

A credit portfolio extract must pass completeness, uniqueness, range and reconciliation controls before modelling.

## Goal

A reusable audit function and exception report for loan records.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 11 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- `loans_dirty.csv`

## Step-by-step

1. Load loans_dirty.csv and define the audit controls.
2. Check required columns and row uniqueness.
3. Measure missingness by column.
4. Test ranges for income, debt-to-income and credit score.

   ```bash
   python starter.py
   ```
5. Write exceptions.csv and audit_summary.json.

   ```bash
   python solution.py
   ```
6. Confirm exception counts reconcile to the summary.

   ```bash
   python -m unittest test_solution.py
   ```

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

The audit identifies every planted defect, produces machine-readable counts and leaves the raw file unchanged.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
