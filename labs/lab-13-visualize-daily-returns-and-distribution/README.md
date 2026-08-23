# Lab 13 — Visualize Daily Returns and Distribution

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO6 / A4 / A5
- Tools: Pandas, Matplotlib, CSV

## Scenario

An investment committee wants to understand daily price changes and the distribution of returns for DBS.

## Goal

A return series, line chart and histogram with labelled analytical takeaways.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 13 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- `dbs_prices.csv`

## Step-by-step

1. Load dbs_prices.csv and sort by Date.
2. Calculate Close.pct_change() as Daily_Return.
3. Drop the first expected NaN from chart input.

   ```bash
   python starter.py
   ```
4. Plot daily returns through time with a zero line.
5. Plot a histogram with mean and tail markers.

   ```bash
   python solution.py
   ```
6. Record mean, standard deviation and largest absolute return.

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

returns.csv has one fewer non-null row than prices; charts render; summary statistics match Pandas calculations.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
