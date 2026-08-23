# Lab 16 — Analyse Statistics, Correlation and Rolling Risk

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO7
- Tools: Pandas, NumPy, Matplotlib, CSV

## Scenario

A portfolio risk analyst must profile returns, compare bank-stock relationships and track changing volatility over time.

## Goal

A statistics table, correlation matrix, rolling-volatility series and drawdown chart.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 16 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- `multi_asset_prices.csv`

## Step-by-step

1. Load multi_asset_prices.csv and calculate daily returns.
2. Compute count, mean, median, standard deviation and quantiles.
3. Calculate covariance and correlation matrices.

   ```bash
   python starter.py
   ```
4. Calculate 20-day rolling volatility and annualise using sqrt(252).
5. Calculate cumulative return and drawdown.

   ```bash
   python solution.py
   ```
6. Check correlation symmetry and drawdown sign conventions.

   ```bash
   python -m unittest test_solution.py
   ```

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

Correlation is symmetric with 1 on the diagonal, rolling volatility has the expected warm-up NaNs, and maximum drawdown is non-positive.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
