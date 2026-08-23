<div align="center">

# Python Programming for Finance

[![Course Code](https://img.shields.io/badge/Course-TGS--2026065049-1f6feb)](https://www.tertiarycourses.com.sg/casl-python-programming-for-finance.html)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Labs](https://img.shields.io/badge/Hands--on_labs-17-18a558)](#hands-on-labs)
[![Duration](https://img.shields.io/badge/Duration-3_days_%C2%B7_24_hours-6f42c1)](https://www.tertiarycourses.com.sg/casl-python-programming-for-finance.html)

**Concept-led WSQ courseware with reproducible, offline-first finance analytics labs.**

[Course page](https://www.tertiarycourses.com.sg/casl-python-programming-for-finance.html) · [Report an issue](https://github.com/tertiarycourses/TGS-2026065049-Python-Programming-for-Finance/issues)

</div>

![Python Programming for Finance course visual](courseware/assets/python-finance-cover-v2.png)

## About this repository

This is the public learner repository for **Python Programming for Finance** (`TGS-2026065049`) by Tertiary Infotech Academy Pte Ltd. The course develops a controlled analytical workflow—from finance requirements and Python fundamentals through data quality, aggregation, visualisation, rolling analysis and an executive evidence pack.

The slide deck is deliberately concept-led. Detailed procedures, exact commands, evidence requirements and acceptance criteria are in the Learner Guide and each lab folder.

## Course topics

1. Introduction to Python Programming
2. Data Types and Operators
3. Problem Solving with Control Structures
4. Scripting with Functions and Lambda
5. Import and Process Finance Data
6. Aggregate and Visualize Finance Data
7. Analyze Finance Data

## Hands-on labs

The 17 labs form a connected learning path:

| Labs | Focus |
|---|---|
| 01–02 | Reproducible setup and translating a finance requirement into an SGX price tool |
| 03–04 | Loan amortisation, collections and portfolio modelling |
| 05–06 | Valuation rules, loops and comprehensions |
| 07–08 | Reusable ratio functions and customer screening |
| 09–11 | Data import, cleaning, filtering and data-quality audit |
| 12–14 | Joins, pivots, returns, distributions and moving-average analysis |
| 15–16 | Auditable pipelines, statistics, correlation, volatility and drawdown |
| 17 | Capstone executive finance analytics pack with automated validation |

Every lab folder contains a scenario, README, PDF guide, starter code, reference solution, checks and the required offline data. Live market-data access is optional and is never required to complete the core lab.

## Repository structure

```text
.
├── courseware/
│   ├── Python Programming for Finance-v1.3.pptx
│   ├── Python Programming for Finance-v1.3.pdf
│   ├── LG-Python Programming for Finance.docx
│   ├── LG-Python Programming for Finance.pdf
│   ├── LP-Python Programming for Finance.docx
│   └── LP-Python Programming for Finance.pdf
└── labs/
    ├── lab-01-set-up-a-reproducible-finance-project/
    ├── ...
    └── lab-17-capstone-produce-an-executive-finance-analytics-pack/
```

## Getting started

Prerequisites:

- Python 3.11 or later
- An editor or notebook environment such as VS Code or JupyterLab
- Permission to create a virtual environment and install the packages listed by a lab

Clone the repository:

```bash
git clone https://github.com/tertiarycourses/TGS-2026065049-Python-Programming-for-Finance.git
cd TGS-2026065049-Python-Programming-for-Finance
```

Then open the lab you are working on and follow its `README.md` or PDF guide. Each lab has its own `requirements.txt`; install only what that lab needs.

## Evidence and responsible use

- Preserve supplied source data and save generated artifacts into the lab's output folder.
- Reconcile totals, validate data types and missing values, and retain the requested screenshots or reports.
- Use only supplied mock data or approved anonymised data in class.
- Examples are educational and are not investment, trading, credit or financial advice.

## Public/private boundary

This repository intentionally excludes assessment question papers, answer keys, trainer-only resources, references, build tooling, QA renders and credentials. Those materials are controlled through the course's authorised learning systems.

## Provider

Developed by **Tertiary Infotech Academy Pte Ltd**<br>
UEN: 201200696W<br>
[www.tertiarycourses.com.sg](https://www.tertiarycourses.com.sg/)

© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.
