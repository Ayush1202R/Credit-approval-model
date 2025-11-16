# 💳 Credit Risk Prediction Model – Lauki Finance

A machine learning–powered Credit Risk Assessment system that predicts the probability of loan default and generates a credit score and rating. The project includes data preprocessing, feature engineering, model training, Optuna hyperparameter tuning, and a fully interactive Streamlit UI.

## 🌐 Live Demo
👉 **[Click here to open the Credit Risk Model](https://credit-approval-model-ml.streamlit.app/)**

## 📌 Overview
This project predicts whether a borrower is likely to default on a loan using demographic, financial, and credit-related inputs. It also generates:
- **Default Probability**
- **Credit Score**
- **Credit Category (Poor / Average / Good / Excellent)**  
Designed for financial institutions to enhance loan evaluation and minimize risk.

## ✨ Key Features
- End-to-end credit risk model  
- Clean and interactive Streamlit interface  
- Takes 10+ borrower inputs  
- Calculates default probability, credit score, and rating  
- Optuna hyperparameter tuning for model optimization  
- Fully deployed and accessible online  

## 🧠 Machine Learning Workflow
- Data Cleaning & Preparation  
- Handling invalid/missing values  
- Encoding categorical features  
- Train-Test Split  
- Logistic Regression Model  
- Optuna Hyperparameter Optimization  
- Evaluation Metrics (AUC, Gini, KS)  
- Saving model using joblib  
- Deployment with Streamlit  

## 📊 Input Parameters
- Age  
- Income  
- Loan Amount  
- Loan Tenure  
- Loan Purpose  
- Avg DPD  
- Delinquency Ratio  
- Credit Utilization Ratio  
- Residence Type  
- Loan Type  
- Number of Open Accounts  

## 🛠 Tech Stack
- **Python**  
- **Scikit-Learn**  
- **Optuna**  
- **Streamlit**  
- **Pandas**  
- **NumPy**  
- **Joblib**

## ▶ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Ayush1202R/Credit-approval-model.git
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run main.py
```


## 📈 Model Output
- **Default Probability (0–1)**  
- **Credit Score (0–900)**  
- **Rating:** Poor / Average / Good / Excellent  

## Author
**Ayush Radharaman Pandey**
