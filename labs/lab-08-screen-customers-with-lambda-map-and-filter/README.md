# Lab 08 — Screen Customers with Lambda, Map and Filter

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO4
- Tools: Python, csv, unittest

## Scenario

A retail bank wants to transform customer income into affordability ratios and filter applications for manual review.

## Goal

A readable transformation pipeline plus an equivalent named-function implementation.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 08 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- `applicants.csv`

## Step-by-step

1. Load applicants.csv and count the input records.
2. Use map with a lambda to add monthly_income.
3. Use filter to select high debt-to-income records.

   ```bash
   python starter.py
   ```
4. Rewrite the risk rule as a named function.
5. Confirm both versions return identical IDs.

   ```bash
   python -m unittest test_solution.py
   ```
6. Explain which implementation is easier to audit.

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

Lambda and named-function pipelines select the same applicant IDs, and counts reconcile to the input.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
