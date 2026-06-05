# Credit Risk Banking System

## Overview

The Credit Risk Banking System is a machine learning-driven application designed to assess the creditworthiness of banking customers and predict the likelihood of loan default. The system analyzes customer financial profiles, credit history, income levels, and other relevant factors to generate risk scores that support data-driven lending decisions.

This project helps financial institutions reduce credit losses, improve loan approval processes, and enhance risk management through predictive analytics.

---


<img width="1536" height="1024" alt="Banking" src="https://github.com/user-attachments/assets/784a7bf9-e377-4151-9dc9-316084b53d4e" />



## Features

* Customer Credit Risk Assessment
* Loan Default Prediction
* Credit Score Generation
* Risk Classification (Low, Medium, High)
* Data Visualization and Reporting
* Real-Time Risk Evaluation
* Historical Data Analysis
* Secure User Authentication
* REST API Integration
* Decision Support Dashboard

---

## Problem Statement

Banks and financial institutions face significant risks when approving loans. Traditional credit evaluation methods can be time-consuming and may not accurately identify high-risk applicants.

This system leverages machine learning algorithms to analyze customer data and predict credit risk, enabling faster and more reliable lending decisions.

---

## Technology Stack

### Backend

* Python
* Flask / FastAPI

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* XGBoost

### Frontend

* HTML
* CSS
* JavaScript
* Bootstrap

### Visualization

* Matplotlib
* Seaborn
* Plotly

---

## Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Risk Prediction
7. Deployment

---

## Project Structure

```text
credit-risk-banking-system/
│
├── data/
├── models/
├── notebooks/
├── src/
│   ├── preprocessing/
│   ├── training/
│   ├── prediction/
│   └── api/
│
├── static/
├── templates/
├── requirements.txt
├── app.py
└── README.md
```

---

## Dataset Features

The model may use the following customer attributes:

* Age
* Annual Income
* Employment Status
* Credit History
* Loan Amount
* Existing Debts
* Number of Credit Accounts
* Payment History
* Debt-to-Income Ratio
* Loan Purpose

---

## Risk Categories

| Risk Score | Category    |
| ---------- | ----------- |
| 0 - 30     | Low Risk    |
| 31 - 70    | Medium Risk |
| 71 - 100   | High Risk   |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/credit-risk-banking-system.git
```

### Navigate to Project

```bash
cd credit-risk-banking-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

