# Consumer Loan Risk & Credit Performance Analysis

---

## Table of Contents

1. [Overview](#overview)
2. [Business Question](#business-question)
3. [Objectives](#objectives)
4. [Dataset](#dataset)
5. [Tools & Technologies](#tools--technologies)
6. [Methodology](#methodology)
7. [Data Cleaning Decisions](#data-cleaning-decisions)
8. [Key Findings](#key-findings)
9. [Visualizations](#visualizations)
10. [Business Implications](#business-implications)
11. [Limitations](#limitations)
12. [Project Structure](#project-structure)
13. [How to Run](#how-to-run)
14. [Author](#author)

---

## Overview

This project analyzes a consumer-loan dataset to understand portfolio composition, loan characteristics, credit grades, and repayment status. The workflow covers data understanding, targeted cleaning, EDA, visualization, and a consolidated, repeatable Python script.

The analysis is **descriptive**. It identifies patterns and comparisons in the available data; it does not establish causation or predict future defaults.

## Business Question

> What borrower and loan characteristics are associated with higher credit risk, loan performance, and repayment problems?

## Objectives

- Understand the structure and quality of the dataset.
- Clean selected fields while preserving meaningful missing values.
- Explore loan status, purpose, loan amount, interest rate, debt-to-income (DTI) ratio, grade, and homeownership.
- Communicate selected portfolio patterns through visualizations.
- Document evidence, implications, and limitations without overstating conclusions.

## Dataset

| Stage | Rows | Columns | Notes |
|---|---:|---:|---|
| Original | 10,000 | 56 | Raw source file; kept unchanged |
| Cleaned | 10,000 | 55 | Index-like `Unnamed: 0` column removed |

The dataset includes borrower attributes, credit-history fields, loan terms and amounts, grades, loan statuses, and repayment-related measures. Field meanings should be verified against the source data dictionary where available.

## Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| pandas | Loading, cleaning, grouping, summary statistics |
| NumPy | Numerical computing support |
| Matplotlib | Static charts |
| Jupyter Notebook | Stepwise exploration and documentation of decisions |
| VS Code | Consolidated, reusable Python script |

## Methodology

1. **Data understanding:** Inspect columns, dimensions, data types, missing values, duplicates, categorical counts, and descriptive statistics.
2. **Data cleaning:** Remove the index-like column, apply targeted missing-value handling, standardize selected text, and convert `issue_month` to datetime.
3. **EDA:** Compare loan status, purpose, amounts, interest rates, DTI ratios, grades, and homeownership.
4. **Visualization:** Create four Matplotlib charts for selected distributions and comparisons.
5. **Scripting:** Consolidate the workflow into a single Python script for repeatable execution.

## Data Cleaning Decisions

| Field / Operation | Action | Reason / Caution |
|---|---|---|
| `Unnamed: 0` | Removed | Unnecessary index-like column |
| `emp_title` | Missing filled with `Unknown`; whitespace trimmed | Makes missing titles explicit and standardizes text |
| `emp_length` | Missing filled with median | Targeted imputation; introduces estimated values |
| `num_accounts_120d_past_due` | Missing filled with `0` | Assumes missing means zero; verify source semantics |
| `debt_to_income` | Missing filled with median | Targeted imputation; may influence group averages |
| Delinquency / inquiry recency fields | Missing filled with `0` | Valid only if source definitions support treating missing as none |
| `issue_month` | Converted to datetime (`%b-%y`) | Enables date-aware handling |
| Joint-application fields | Missing values retained | May be not applicable to individual applications; avoids inventing values |
| Duplicates | Checked after cleaning | 0 exact duplicate rows found |

> **Caution:** Imputing a missing recency or delinquency value with zero is appropriate only if the dataset documentation supports that interpretation.

## Key Findings

| Finding | Evidence | Limitation |
|---|---|---|
| Portfolio is dominated by **Current** loans | 9,375 of 10,000 loans (93.75%) | Current status does not guarantee eventual repayment; loan age and timing matter |
| **Debt consolidation** is the most common purpose | 5,144 loans | Frequency alone does not establish profitability or risk |
| Interest rates generally **rise from Grade A toward Grade G** | Grouped mean rates show an upward pattern | Descriptive association; does not establish cause |
| Average loan amount **varies by purpose and status** | Group means computed in EDA | Exact values should be taken from executed notebook output |
| Average DTI **differs by loan status** | Group means computed in EDA | Averages alone do not establish predictive power or causation |

> **Rare-status note:** Only 7 loans are classified as *Charged Off*. This sample is too small for strong generalizations; sample sizes should accompany any discussion of rare statuses.

## Visualizations

| Chart | Purpose |
|---|---|
| Loan Status Distribution | Number of loans in each status category |
| Loan Purpose Distribution | Most frequent loan purposes |
| Average Interest Rate by Loan Grade | Average interest rates across grades |
| Average Loan Amount by Purpose | Average loan amounts across purposes |

Charts should be interpreted alongside category counts and data limitations, especially where sample sizes are small.

## Business Implications

- Portfolio composition can be summarized through loan-status and loan-purpose distributions.
- Grade-level interest-rate differences can be reviewed as evidence of pricing differentiation, without assuming causation.
- Differences in loan amounts and DTI ratios can guide further investigation but do not prove default risk.
- Rare outcomes require cautious interpretation and additional evidence before operational decisions.

## Limitations

- Descriptive analysis only; no default prediction or causal inference.
- Only seven *Charged Off* records, which limits analysis of that outcome.
- Imputation decisions can influence summary statistics.
- Joint-application fields retain missing values because they may not apply to individual applications.
- Time coverage, sampling method, and field definitions should be verified before making broader claims.
- The *Current* share must not be interpreted as a default rate or as proof of low risk.

## Project Structure

```
consumer-loan-risk-analysis/
├── Documentation/
│   └── Project_documentation.pdf
├── Scripts/
│   └── loan_analysis.py             # consolidated analysis script
├── data/
│   ├── Loans.csv                    # raw source; keep unchanged
│   └── Loans_Cleaned.csv            # exported after cleaning
├── notebooks/
│   ├── 01_Data-Understanding.ipynb
│   ├── 02_Data-Cleaning.ipynb
│   ├── 03_EDA.ipynb
│   └── 04_Visualization.ipynb
└── README.md
```

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/akash8kj/<repo-name>.git
cd <repo-name>

# 2. Install dependencies
pip install pandas numpy matplotlib jupyter

# 3. Run the consolidated script
python Scripts/loan_analysis.py
```

To follow the analysis step by step, open the notebooks in order (`01` to `04`) using Jupyter Notebook.

## Author

**Ankan Mondal**
BCA Student, | Aspiring Data Analyst

