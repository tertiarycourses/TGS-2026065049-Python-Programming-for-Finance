# Lab 02 — Translate a Finance Requirement into an SGX Price Tool

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO1
- Tools: Python, CSV, optional yfinance

## Scenario

A wealth desk wants a repeatable daily price summary for a small basket of Singapore-listed equities.

## Goal

A requirement canvas, acceptance tests and an offline-safe SGX price summary script.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 02 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- `sgx_prices.csv`

## Step-by-step

1. Read scenario.md and identify users, inputs, rules, outputs and risks.
2. Complete requirement_canvas.md before coding.
3. Run the starter against the supplied fallback prices.

   ```bash
   python starter.py
   ```
4. Implement load_prices() and format_report() in solution.py.
5. Add a test for the invalid ticker row.

   ```bash
   python -m unittest test_solution.py
   ```
6. Save the output as evidence.txt.

   ```bash
   python solution.py > evidence.txt
   ```

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

The report prints five labelled SGX prices to two decimals, handles an invalid ticker without crashing, and all tests pass.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
