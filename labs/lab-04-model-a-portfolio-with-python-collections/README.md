# Lab 04 — Model a Portfolio with Python Collections

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO2
- Tools: Python, csv

## Scenario

An investment team needs a clean in-memory representation of holdings, identifiers, sector groups and prices.

## Goal

A portfolio report using list, tuple, dictionary and set operations.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 04 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- `portfolio.csv`

## Step-by-step

1. Inspect portfolio.csv and identify suitable Python types.
2. Load rows into a list of dictionaries.

   ```bash
   python starter.py
   ```
3. Represent the fixed instrument key as a tuple.
4. Build ticker-to-price and ticker-to-sector dictionaries.
5. Use sets to calculate overlap between two portfolios.
6. Print market value and weights; confirm weights total 100%.

   ```bash
   python solution.py
   ```

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

Every holding has a market value, portfolio weights sum to 100%, and the overlap set is reported without duplicates.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
