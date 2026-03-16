import pandas as pd
import numpy as np

np.random.seed(42)

rows = 10000

data = pd.DataFrame({
    "age": np.random.randint(21, 65, rows),
    "income": np.random.randint(20000, 120000, rows),
    "employment_years": np.random.randint(0, 30, rows),
    "loan_amount": np.random.randint(1000, 50000, rows),
    "debt": np.random.randint(0, 40000, rows),
    "credit_accounts": np.random.randint(1, 10, rows),
    "late_payments": np.random.randint(0, 6, rows),
    "credit_history_years": np.random.randint(1, 20, rows),
})

# Feature engineering
data["debt_to_income"] = data["debt"] / data["income"]
data["loan_to_income"] = data["loan_amount"] / data["income"]

# Create target variable (simplified rule-based creditworthiness)
data["creditworthy"] = (
    (data["debt_to_income"] < 0.4) &
    (data["late_payments"] < 2) &
    (data["credit_history_years"] > 3)
).astype(int)

data.to_csv("data/credit_data.csv", index=False)

print("Dataset created with", len(data), "rows")