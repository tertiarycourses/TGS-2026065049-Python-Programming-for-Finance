# Lab 06 — Loop Through a Portfolio and Build Comprehensions

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO3
- Tools: Python, csv

## Scenario

A portfolio analyst needs valuations for every valid position while malformed records are logged and excluded.

## Goal

A reconciled holdings table, exception log and concise list/dict comprehensions.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 06 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- `holdings.csv`

## Step-by-step

1. Inspect holdings.csv and find the deliberately malformed row.
2. Iterate with enumerate() to number records.
3. Use continue to skip and log the malformed holding.
4. Accumulate total value and verify it against the output rows.

   ```bash
   python solution.py
   ```
5. Create a list comprehension for overweight positions.
6. Create a dictionary comprehension for ticker-to-weight mapping.

   ```bash
   python -m unittest test_solution.py
   ```

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

The invalid row is logged once, valid positions reconcile to the portfolio total, and comprehension results match the loop results.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
