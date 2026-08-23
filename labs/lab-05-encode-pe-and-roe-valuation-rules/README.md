# Lab 05 — Encode PE and ROE Valuation Rules

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO3
- Tools: Python, unittest

## Scenario

An equity screen must classify securities consistently at defined PE and ROE thresholds.

## Goal

A boundary-tested BUY/HOLD/REVIEW valuation classifier.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 05 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- No external dataset required.

## Step-by-step

1. Read the valuation policy and underline every boundary.
2. Run the starter with PE values 14.99, 15, 25 and 25.01.

   ```bash
   python starter.py
   ```
3. Implement classify_valuation() with explicit inclusive boundaries.
4. Combine PE and ROE conditions into the final recommendation.
5. Run boundary tests.

   ```bash
   python -m unittest test_solution.py
   ```
6. Explain one classification in evidence.txt.

   ```bash
   python solution.py > evidence.txt
   ```

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

All exact-boundary tests pass and each recommendation includes the rule that produced it.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
