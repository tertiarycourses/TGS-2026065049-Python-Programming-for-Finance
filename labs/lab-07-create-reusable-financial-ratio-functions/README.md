# Lab 07 — Create Reusable Financial Ratio Functions

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO4
- Tools: Python, dataclasses, unittest

## Scenario

A bank reporting team calculates margin, ROE and ROA in several reports and needs one tested implementation.

## Goal

A ratios module returning named results with validation and tests.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 07 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- No external dataset required.

## Step-by-step

1. Review the required function contract and units.
2. Implement safe_divide() with a defensible zero-denominator result.
3. Implement net_margin(), roe() and roa().
4. Return a dictionary of named ratios from calculate_ratios().

   ```bash
   python solution.py
   ```
5. Test typical, zero and negative cases.

   ```bash
   python -m unittest test_solution.py
   ```
6. Document assumptions in evidence.txt.

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

The sample produces margin about 55.95%, ROE about 18.09% and ROA about 1.53%; tests pass.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
