# Credit Scoring Model

A machine learning project that predicts the creditworthiness of individuals using past financial data, with detailed reports for multiple borrowers.

The goal of this project is to simulate how financial institutions evaluate whether a borrower is likely to repay a loan. The model analyzes financial features such as income, debts, credit history, and payment behavior to classify borrowers as creditworthy or high risk. Users can evaluate multiple individuals at once and see all input details along with eligibility.

---

## Project Overview

Credit scoring is widely used by banks, fintech companies, and lending institutions to evaluate loan applications. In this project, we build a machine learning pipeline that processes financial data and predicts borrower risk using multiple classification algorithms.

The project includes data preprocessing, feature engineering, model training, and evaluation using standard machine learning metrics. It also provides a reporting system to test multiple individuals and show their financial ratios and credit eligibility.

---

## Features Used

The dataset includes financial attributes commonly used in credit risk analysis:

- Age
- Income
- Employment Years
- Loan Amount
- Debt
- Credit Accounts
- Late Payments
- Credit History Length

### Engineered Features

Additional financial indicators were created to improve prediction quality:

- **Debt-to-Income Ratio**
- **Loan-to-Income Ratio**

These ratios are widely used in real-world credit risk analysis.

---

## Machine Learning Models

The following classification algorithms were implemented:

- Logistic Regression
- Decision Tree
- Random Forest

Each model is trained and evaluated to compare performance.

---

## Model Evaluation

Model performance is measured using standard classification metrics:

- Precision
- Recall
- F1 Score
- ROC-AUC Score

These metrics help evaluate how well the model distinguishes between creditworthy and risky borrowers.

---

## Individual Credit Prediction

The project now supports predicting creditworthiness for multiple individuals at once. For each person, the following is displayed:

- Full financial info
- Debt-to-Income ratio
- Loan-to-Income ratio
- Credit eligibility (Creditworthy / High Risk)

This makes it easy to take snapshots of results or integrate into reporting dashboards.

---

## Project Structure


credit-scoring-model
│
├── data
│ ├── credit_data.csv
│ └── generate_dataset.py
│
├── src
│ ├── init.py
│ ├── preprocess.py
│ ├── train_model.py
│ └── evaluate_model.py
│
├── main.py
├── predict.py
├── requirements.txt
└── README.md


---

## Installation

Clone the repository:

```bash
git clone https://github.com/noumanshakeel555-lang/credit-scoring-model

Install dependencies:

pip install -r requirements.txt
Running the Project

Generate the dataset:

python data/generate_dataset.py

Run the full pipeline and evaluate models:

python main.py

Predict creditworthiness for multiple individuals:

python predict.py

The program will display all input financial info, calculated ratios, and credit eligibility for each individual.

Future Improvements

Possible extensions for this project include:

Hyperparameter tuning

Cross-validation

Model explainability using SHAP

Feature importance visualization

Credit scoring (e.g., 300–850)

Building a web interface with Streamlit

Deploying the model as an API

Author

Muhammad Nouman Shakeel

GitHub:
https://github.com/noumanshakeel555-lang

License

This project is open source and available under the MIT License.
