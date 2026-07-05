# 🛡️ FraudShield AI
### Intelligent Fraud Detection & Transaction Risk Analysis System

FraudShield AI is an intelligent fraud detection and transaction risk analysis system designed to help banks, fintech companies, payment processors, and financial institutions identify potentially fraudulent transactions in real time.

The application combines a **Machine Learning model** with a **Large Language Model (LLM)** to provide not only accurate fraud predictions but also transparent explanations and actionable recommendations for fraud analysts and risk teams.

> **Hackathon Use Case:** Transaction Fraud Monitoring (Finance Domain)

---

# 📌 Project Overview

Financial institutions process thousands of transactions every day, making it difficult for fraud analysts to manually detect suspicious activities.

FraudShield AI addresses this challenge by providing an AI-powered decision-support system that:

- Detects suspicious transactions using Machine Learning
- Calculates fraud probability and transaction risk
- Explains why a transaction is considered suspicious using an LLM
- Recommends appropriate investigation actions
- Automatically sends email alerts for high-risk transactions

The solution is designed to support operational decision-making and does **not** automatically block customers or make final financial decisions.

---

# 🚀 Features

- ✅ Real-time fraud prediction
- ✅ Fraud probability and risk score calculation
- ✅ Risk classification (Low, Medium, High)
- ✅ AI-generated explanations using Groq LLM
- ✅ Investigation recommendations
- ✅ Automatic email alerts for high-risk transactions
- ✅ Interactive web interface
- ✅ Explainable AI for improved transparency

---

# ⚙️ How It Works

## Step 1 – Transaction Input

The user enters transaction information including:

- Transaction Amount
- Transaction Type
- Sender Account
- Receiver Account
- Transaction Time
- Sender Balance Before Transaction
- Receiver Balance Before Transaction

---

## Step 2 – Feature Engineering

The application automatically computes additional features, including:

- Sender Balance After Transaction
- Receiver Balance After Transaction

The processed transaction data is then prepared for the trained Machine Learning model.

---

## Step 3 – Fraud Prediction

A trained CatBoost model evaluates the transaction and predicts whether it is:

- Legitimate
- Fraudulent

The model also generates a fraud probability.

---

## Step 4 – Risk Assessment

The fraud probability is converted into a numerical risk score and categorized as:

| Risk Score | Risk Level |
|------------|------------|
| Low | Low Risk |
| Medium | Medium Risk |
| High | High Risk |

This allows fraud analysts to quickly understand the severity of each transaction.

---

## Step 5 – AI Explanation

FraudShield AI integrates the **Groq Large Language Model (LLM)** to generate a clear explanation for every prediction.

Instead of displaying only a prediction result, the AI explains:

- Why the transaction is suspicious
- Key fraud indicators
- Possible transaction patterns
- Recommended next steps for investigators

This improves model transparency and supports informed decision-making.

---

## Step 6 – Email Alert

For high-risk transactions, the system automatically sends an email containing:

- Fraud prediction
- Risk score
- Transaction summary
- Sender information
- Receiver information
- Account balances
- AI-generated explanation
- Investigation recommendations

This enables rapid notification and faster incident response.

---

# 🧠 Technology Stack

| Technology | Purpose |
|------------|----------|
| Flask | Web Application Framework |
| CatBoost | Fraud Detection Model |
| Scikit-learn | Machine Learning Utilities |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Joblib | Model Loading |
| Groq API | AI Explanations |
| HTML/CSS/Bootstrap | User Interface |

---

# 📂 Project Structure

```
FraudShield_AI_ML_Hackathon_2026/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── raw/
│   ├── processed/
│  
│
├── models/
│
├── notebooks/
│
├── src/
│
├── templates/
│
├── static/
│
├── presentation/
│

```

---

# 🏗️ System Workflow

```
User Input
      │
      ▼
Input Validation
      │
      ▼
Feature Engineering
      │
      ▼
Machine Learning Model
      │
      ▼
Fraud Prediction
      │
      ▼
Risk Score Calculation
      │
      ▼
Groq LLM Explanation
      │
      ▼
Recommendations
      │
      ▼
     Risk?
      │
 ┌────┴─────┐
 │          │
No         Yes
 │          │
 ▼          ▼
Display   Send Email Alert
```

---

# 💡 AI Implementation

FraudShield AI combines predictive analytics with explainable AI.

### Machine Learning

The CatBoost model analyzes transaction features and predicts whether a transaction is fraudulent.

### Large Language Model (LLM)

The Groq API generates human-readable explanations based on the model prediction, transaction details, and risk indicators.

The LLM is used to:

- Explain prediction results
- Highlight suspicious patterns
- Generate investigation recommendations
- Improve transparency and user trust

---

# 📊 Output

For every transaction, the application provides:

- Fraud Prediction
- Fraud Probability
- Risk Score
- Risk Level
- AI Explanation
- Recommended Actions

High-risk transactions additionally trigger an automated email notification.

---

# 🔒 Responsible AI

FraudShield AI is designed as a **decision-support tool**.

The system:

- Does **not** automatically block accounts
- Does **not** deny financial services
- Provides recommendations for human review
- Uses explainable AI to improve transparency
- Supports fraud analysts rather than replacing them

---

# 🎯 Use Case

**Finance Domain – Transaction Fraud Monitoring**

FraudShield AI helps financial institutions:

- Detect suspicious transaction behaviour
- Understand fraud-risk indicators
- Review affected accounts
- Prioritize investigations
- Improve fraud response time

---

# 🔮 Future Improvements

Potential future enhancements include:

- Real-time streaming fraud detection
- Graph-based mule account detection
- User behaviour analytics
- API integration with banking systems
- Analyst feedback loop for model retraining
- SMS and push notification alerts
- Fraud analytics dashboard
- Model monitoring and drift detection

---

# 📌 Conclusion

FraudShield AI goes beyond traditional fraud detection by combining machine learning with explainable AI, automated reporting, and an intuitive web interface.

Rather than simply identifying fraudulent transactions, the system helps users understand *why* a transaction is suspicious and provides practical recommendations to support timely, informed, and responsible decision-making.

---

# 🚀 Live AI Solution

FraudShield AI is deployed as a fully functional web application.

🔗 **Live Dashboard:**  
https://fraudshieldai.hostless.app/

## Features available in the live system:
- 🔍 Real-time fraud prediction
- 📊 Risk score classification (Low / Medium / High)
- 🧠 Explainable AI insights using LLM
- 📩 Recommended investigation actions
- ⚠️ High-risk transaction alerts

---

## 👨‍💻 Developed For

**AI/ML Hackathon Challenge 2026**

**Finance Domain – Transaction Fraud Monitoring**
