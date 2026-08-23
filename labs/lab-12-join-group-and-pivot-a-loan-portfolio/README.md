# Lab 12 — Join, Group and Pivot a Loan Portfolio

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO6
- Tools: Pandas, CSV

## Scenario

A risk team needs exposure and approval metrics by sector, region and risk band from separate application and reference tables.

## Goal

A validated merge, groupby summary and pivot table exported to CSV.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 12 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- `loan_applications.csv`
- `sector_reference.csv`

## Step-by-step

1. Profile application and sector reference keys.
2. Merge with validate='many_to_one' and indicator=True.
3. Review unmatched rows before dropping or fixing them.

   ```bash
   python starter.py
   ```
4. Group by sector and calculate count, exposure and mean credit score.
5. Create a region-by-risk-band exposure pivot.

   ```bash
   python solution.py
   ```
6. Reconcile grouped and pivot totals to the merged portfolio.

   ```bash
   python -m unittest test_solution.py
   ```

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

No unexpected many-to-many join occurs, unmatched keys are reported, and summary exposure totals equal the source.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
