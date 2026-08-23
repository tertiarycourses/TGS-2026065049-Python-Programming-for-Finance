# Lab 03 — Build a Loan Amortisation Calculator

## Alignment

- Course: Python Programming for Finance (`TGS-2026065049`)
- Outcome / assessment: LO2
- Tools: Python, math, csv

## Scenario

A relationship manager needs a transparent monthly-instalment calculation including the zero-interest staff-loan case.

## Goal

A loan calculator with monthly payment, total repayment and total interest.

## Folder contents

- `README.md` — this detailed lab guide
- `Lab 03 Guide.pdf` — portable mirror of this guide
- `starter.py` — learner starting file
- `solution.py` — working reference implementation
- `test_solution.py` — automated checks where applicable
- No external dataset required.

## Step-by-step

1. Open scenario.md and note the principal, annual rate and term.
2. Run the starter and observe the incomplete result.

   ```bash
   python starter.py
   ```
3. Implement the amortisation formula in monthly_payment().
4. Handle a zero annual rate without division by zero.
5. Generate the first 12 schedule rows.

   ```bash
   python solution.py
   ```
6. Run the unit tests and save the output.

   ```bash
   python -m unittest test_solution.py
   ```

## Evidence to capture

- Terminal output or test result
- Generated CSV/chart/report requested by the lab
- One sentence explaining what the result means for the finance scenario

## Acceptance criteria

For $500,000 at 2.6% over 25 years, payment is about $2,268.35; a 0% loan returns principal divided by months.

## Troubleshooting

- Run commands from this lab folder so relative file paths resolve correctly.
- If a package is missing, install it in the lab environment and record the version.
- If output differs, first verify row counts, data types, date order, units and missing values.
- The supplied market data is deterministic and works offline; optional live-data refreshes may differ.
