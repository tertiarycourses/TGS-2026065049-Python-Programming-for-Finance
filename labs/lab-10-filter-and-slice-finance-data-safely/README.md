# Lab 10 — Filter and Slice Finance Data Safely

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO5
- Tools: Pandas, CSV

## Scenario

A portfolio manager asks for bank-sector positions above a materiality threshold and a date-windowed price series.

## Goal

A filtered positions file and labelled versus positional slice comparison.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 10 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- `portfolio.csv`
- `market_prices.csv`

## Step-by-step

1. Load portfolio.csv and market_prices.csv.
2. Use loc with a boolean mask for Bank sector and Value above threshold.
3. Use loc for an inclusive date-label slice.
4. Use iloc for a positional sample and compare endpoints.

   ```bash
   python starter.py
   ```
5. Sort without mutating the original DataFrame.
6. Save filtered_positions.csv and run tests.

   ```bash
   python -m unittest test_solution.py
   ```

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

The filter returns only qualifying bank positions; loc and iloc row counts match their documented boundary rules.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
