import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. DATA UNDERSTANDING
# ============================================================

df = pd.read_csv("Loans.csv")

print("\n========== DATA UNDERSTANDING ==========\n")

print("Column Names:")
print(df.columns)

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum().sort_values(ascending=False))

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nCategorical Columns - Value Counts:")

for col in ['homeownership', 'verified_income', 'loan_purpose',
            'application_type', 'term', 'grade', 'loan_status']:
    print("\n", col)
    print(df[col].value_counts(dropna=False))

print("\nDescriptive Statistics:")
print(df.describe().T)

print("\nSelected Numeric Statistics:")
print(df[['annual_income',
          'debt_to_income',
          'loan_amount',
          'interest_rate',
          'installment',
          'total_credit_limit',
          'total_credit_utilized',
          'paid_total',
          'paid_principal',
          'paid_interest',
          'paid_late_fees']].describe())

print("\nLoan Status Percentage:")
print(df['loan_status'].value_counts(normalize=True) * 100)


# ============================================================
# 2. DATA CLEANING
# ============================================================

print("\n========== DATA CLEANING ==========\n")

# Remove unnecessary index column
df.drop(columns=['Unnamed: 0'], inplace=True)

# Handle missing values in selected columns
df['emp_title'] = df['emp_title'].fillna('Unknown')

df['emp_length'] = df['emp_length'].fillna(
    df['emp_length'].median()
)

df['num_accounts_120d_past_due'] = df[
    'num_accounts_120d_past_due'
].fillna(0)

df['debt_to_income'] = df['debt_to_income'].fillna(
    df['debt_to_income'].median()
)

# Clean text values
df['emp_title'] = df['emp_title'].str.strip()

# Convert issue month to datetime
df['issue_month'] = pd.to_datetime(
    df['issue_month'],
    format='%b-%y'
)

# Missing values representing no previous delinquency/inquiry
df['months_since_last_delinq'] = df[
    'months_since_last_delinq'
].fillna(0)

df['months_since_90d_late'] = df[
    'months_since_90d_late'
].fillna(0)

df['months_since_last_credit_inquiry'] = df[
    'months_since_last_credit_inquiry'
].fillna(0)

# Joint application columns are kept missing because
# they are not applicable to individual applications.

print("Remaining Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows After Cleaning:")
print(df.duplicated().sum())


# ============================================================
# 3. EXPLORATORY DATA ANALYSIS
# ============================================================

print("\n========== EXPLORATORY DATA ANALYSIS ==========\n")

df_clean = df.copy()

print("Loan Status Distribution:")
print(df_clean['loan_status'].value_counts())

print("\nLoan Purpose Distribution:")
print(df_clean['loan_purpose'].value_counts())

print("\nLoan Amount Summary:")
print(df_clean['loan_amount'].describe())

print("\nAverage Loan Amount by Purpose:")
print(
    df_clean.groupby('loan_purpose')['loan_amount']
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Loan Amount by Loan Status:")
print(
    df_clean.groupby('loan_status')['loan_amount']
    .mean()
    .sort_values(ascending=False)
)

print("\nInterest Rate Summary:")
print(df_clean['interest_rate'].describe())

print("\nAverage Interest Rate by Grade:")
print(
    df_clean.groupby('grade')['interest_rate']
    .mean()
    .sort_values()
)

print("\nAverage Debt-to-Income by Loan Status:")
print(
    df_clean.groupby('loan_status')['debt_to_income']
    .mean()
    .sort_values()
)

print("\nLoan Grade vs Loan Status:")
print(
    df_clean.groupby('grade')['loan_status']
    .value_counts()
)

print("\nHomeownership vs Loan Status:")
print(
    df_clean.groupby('homeownership')['loan_status']
    .value_counts()
)


# ============================================================
# 4. VISUALIZATION
# ============================================================

print("\n========== VISUALIZATION ==========\n")


# 1. Loan Status Distribution
df_clean['loan_status'].value_counts().plot(kind='bar')

plt.title('Loan Status Distribution')
plt.xlabel('Loan Status')
plt.ylabel('Number of Loans')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 2. Loan Purpose Distribution
df_clean['loan_purpose'].value_counts().plot(kind='bar')

plt.title('Loan Purpose Distribution')
plt.xlabel('Loan Purpose')
plt.ylabel('Number of Loans')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 3. Average Interest Rate by Loan Grade
df_clean.groupby('grade')['interest_rate'].mean().plot(
    kind='bar'
)

plt.title('Average Interest Rate by Loan Grade')
plt.xlabel('Loan Grade')
plt.ylabel('Average Interest Rate (%)')
plt.tight_layout()
plt.show()


# 4. Average Loan Amount by Purpose
df_clean.groupby('loan_purpose')['loan_amount'].mean() \
    .sort_values() \
    .plot(kind='barh')

plt.title('Average Loan Amount by Purpose')
plt.xlabel('Average Loan Amount')
plt.ylabel('Loan Purpose')
plt.tight_layout()
plt.show()


# ============================================================
# 5. FINAL CHECK
# ============================================================

print("\n========== FINAL CHECK ==========\n")

print("Final Dataset Shape:")
print(df.shape)

print("\nFinal Duplicate Count:")
print(df.duplicated().sum())

print("\nScript executed successfully.")