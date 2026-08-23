# Lab 09 — Import and Clean a Finance DataFrame

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO5
- Tools: Pandas, CSV

## Scenario

A treasury extract contains duplicated dates, missing prices and inconsistent date/value types.

## Goal

A curated price DataFrame and a written data-quality reconciliation.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 09 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- `dirty_prices.csv`

## Step-by-step

1. Load dirty_prices.csv with Pandas and inspect head, info and dtypes.
2. Parse Date and coerce numeric price columns.
3. Measure duplicates and missing values before changing data.

   ```bash
   python starter.py
   ```
4. Remove duplicate dates using the latest record.
5. Fill only short Close-price gaps and document the assumption.
6. Save clean_prices.csv and quality_report.txt.

   ```bash
   python solution.py
   ```

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

The curated file has unique sorted dates, numeric prices, no missing Close values, and a reconciliation from raw to clean rows.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
