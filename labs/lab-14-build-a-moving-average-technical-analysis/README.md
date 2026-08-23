# Lab 14 — Build a Moving-Average Technical Analysis

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO6 / A2–A3 / A6–A9
- Tools: Pandas, Matplotlib, optional yfinance

## Scenario

A quantitative analyst needs an OHLC view and 10/50-day moving averages with objectively detected crossover dates.

## Goal

An offline-safe technical-analysis report with OHLC, moving averages and crossover evidence.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 14 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- `dbs_prices.csv`

## Step-by-step

1. Load the supplied DBS OHLC data; optionally refresh with yfinance.
2. Validate required OHLC columns and date ordering.
3. Calculate MA10 and MA50 with rolling().mean().

   ```bash
   python starter.py
   ```
4. Detect sign changes in MA10 minus MA50.
5. Plot Close, MA10 and MA50 with crossover markers.

   ```bash
   python solution.py
   ```
6. Save crossover_dates.csv and explain the first crossover.

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

The output contains OHLC rows, MA10/MA50 values, at least one crossover date, and a labelled chart; the offline file always works.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
