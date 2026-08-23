# Lab 01 — Set Up a Reproducible Finance Project

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO1 / A1
- Tools: Python 3, uv or venv, Pandas, Matplotlib

## Scenario

A bank analytics team needs every learner to run the same package versions and verify the environment before analysing SGX data.

## Goal

A verified Python project with an environment check and dependency record.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 01 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- No external dataset required.

## Step-by-step

1. Create the lab project folder and open a terminal in it.

   ```bash
   uv init python-finance-lab01
   ```
2. Add the analysis packages.

   ```bash
   uv add pandas numpy matplotlib yfinance
   ```
3. Create env_check.py from the supplied starter file.

   ```bash
   cp starter.py env_check.py
   ```
4. Run the environment check.

   ```bash
   uv run python env_check.py
   ```
5. Record the Python and package versions in evidence.txt.

   ```bash
   uv tree > evidence.txt
   ```
6. Review the output for missing packages or tracebacks.

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

The script prints the Python, Pandas, NumPy and Matplotlib versions and ends with ENVIRONMENT READY.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
