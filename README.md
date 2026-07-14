# 💳 Credit Risk Prediction Model — Lauki Finance

[![GitHub license](https://img.shields.io/github/license/Ayush1202R/Credit-approval-model?style=flat-square)](https://github.com/Ayush1202R/Credit-approval-model/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Ayush1202R/Credit-approval-model?style=flat-square)](https://github.com/Ayush1202R/Credit-approval-model/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/Ayush1202R/Credit-approval-model/pulls)
[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-brightgreen?style=flat-square)](https://credit-approval-model-ml.streamlit.app/)

An end-to-end Machine Learning–powered credit risk assessment system built to predict the probability of default, assign credit scores, and categorize loan applications. 

Features data preprocessing, categorical encoding, model training, Optuna hyperparameter optimization, and a fully interactive Streamlit UI.

---

## 🌟 Key Features

* **Default Probability Estimator**: Uses a Logistic Regression classifier optimized using Optuna.
* **Credit Scoring Algorithm**: Translates default probability into a standard credit score ranging from $300$ to $900$.
* **Risk Categorization**: Automatically groups applicants into ratings: `Poor`, `Average`, `Good`, or `Excellent` risk profiles.
* **Tuning Pipelines**: Pre-configured hyperparameter optimization loops using Optuna for maximum precision.
* **Interactive Form Dashboard**: Streamlit interface taking demographic, financial, and credit-history parameters.

---

## 📊 Evaluation Parameters

The system evaluates credit risk using 11 key parameters:
1. **Age**: Applicant age (years).
2. **Income**: Annual gross earnings ($).
3. **Loan Amount**: Requested loan amount ($).
4. **Loan Tenure**: Requested repayment duration (months).
5. **Loan Purpose**: Categorical reason for borrowing.
6. **Average DPD (Days Past Due)**: History of delayed payments.
7. **Delinquency Ratio**: Ratio of past delinquent accounts.
8. **Credit Utilization Ratio**: Percentage of revolving credit limit used.
9. **Residence Type**: Owner / Renting status.
10. **Loan Type**: Secured / Unsecured loan category.
11. **Number of Open Accounts**: Active borrowing accounts.

---

## 📂 Project Structure

```text
Credit-approval-model/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── artifacts/              # Pre-trained models and scaler states
├── CONTRIBUTING.md
├── LICENSE                  # MIT License
├── main.py                  # Model training and Optuna optimization pipeline
├── main_1.py                # Streamlit dashboard interface
├── prediction_helper.py     # Utility functions for predictions and credit scoring
├── README.md                # Documentation
└── requirements.txt         # Dependencies
```

---

## 🛠️ Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Ayush1202R/Credit-approval-model.git
cd Credit-approval-model
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run main_1.py
```
