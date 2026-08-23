# Lab 17 — Capstone: Produce an Executive Finance Analytics Pack

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO1–LO7
- Tools: Python, Pandas, Matplotlib, HTML

## Scenario

The CFO requests a concise, reproducible evidence pack combining data quality, portfolio exposure, returns, risk and recommendations.

## Goal

A self-contained HTML report, charts, curated CSVs, validation log and executive summary.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 17 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- `capstone_portfolio.csv`
- `multi_asset_prices.csv`

## Step-by-step

1. Review the acceptance checklist and supplied portfolio data.
2. Run the data-quality audit and save the reconciliation.
3. Calculate position values, weights and sector exposure.
4. Calculate return, volatility and drawdown indicators.

   ```bash
   python starter.py
   ```
5. Generate charts and the HTML executive report.

   ```bash
   python solution.py
   ```
6. Run validate_outputs.py and capture PASS evidence.

   ```bash
   python validate_outputs.py
   ```

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

All required files exist, totals reconcile, charts have labels, the HTML report opens locally, and validate_outputs.py prints CAPSTONE PASS.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
