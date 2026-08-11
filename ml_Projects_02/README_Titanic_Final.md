# 🚢 Titanic Survival Predictor — Logistic Regression

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![Accuracy](https://img.shields.io/badge/Accuracy-82.03%25-brightgreen)
![Status](https://img.shields.io/badge/Status-Live-success)

> A machine learning web app that predicts whether a Titanic passenger would have survived — built with Python, Scikit-learn, and deployed on Streamlit Cloud.

🔗 **Live App:** [Click here to try it](https://your-app-link.streamlit.app)

---

## 📌 Project Overview

This project uses passenger information (age, class, sex, fare, etc.) to predict survival on the Titanic. A classic binary classification problem demonstrating end-to-end ML skills — data cleaning, encoding, scaling, model training, evaluation, and live deployment.

---

## 🎯 Problem Statement

> Given passenger details, can we predict whether they would have survived the Titanic disaster?
> **1 = Survived | 0 = Did Not Survive**

---

## 📊 Dataset

| Detail | Info |
|---|---|
| Source | Kaggle — Titanic Dataset |
| Total Records | 891 passengers |
| Target Variable | Survived (0 or 1) |

---

## 🔧 Features Used

| Feature | Description |
|---|---|
| Pclass | Passenger class (1st, 2nd, 3rd) |
| Sex | Gender — encoded (Male=0, Female=1) |
| Age | Age of passenger |
| SibSp | Siblings / Spouse aboard |
| Parch | Parents / Children aboard |
| Fare | Ticket price paid |
| Embarked | Port (C=0, Q=1, S=2) |

---

## 🧹 Data Preprocessing

| Step | Action |
|---|---|
| Missing Age | Filled with median value |
| Missing Embarked | Filled with mode |
| Cabin column | Dropped (too many nulls) |
| Name / Ticket / ID | Dropped (not useful) |
| Sex & Embarked | Label Encoded |
| All features | StandardScaler applied |

---

## 🧪 Model Performance

| Metric | Score |
|---|---|
| **Accuracy** | **82.03%** |
| **Precision** | **80.73%** |
| **Recall** | **76.86%** |

> 💡 Industry benchmark for Titanic dataset is 78–85% accuracy. Our model sits right in that range!

### Confusion Matrix Explained

| | Predicted: No | Predicted: Yes |
|---|---|---|
| **Actual: No** | True Negative ✅ | False Positive ❌ |
| **Actual: Yes** | False Negative ❌ | True Positive ✅ |

---

## 💡 Key Insights

- **Sex** is the strongest predictor — females had much higher survival rates
- **Pclass** is second — 1st class passengers survived significantly more
- **Age** matters — children were given priority
- **Fare** correlates with class and therefore survival rate

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas & NumPy | Data cleaning & manipulation |
| Matplotlib & Seaborn | Data visualization & confusion matrix |
| Scikit-learn | ML model, LabelEncoder, StandardScaler |
| Pickle | Model & scaler serialization |
| Streamlit | Web app & deployment |
| GitHub | Version control |

---

## 📈 ML Pipeline

```
Raw Titanic CSV
    ↓
Exploratory Data Analysis (EDA)
    ↓
Data Cleaning (nulls, dropped columns)
    ↓
Label Encoding (Sex, Embarked)
    ↓
Feature Scaling (StandardScaler)
    ↓
Train / Test Split (80% / 20%)
    ↓
Logistic Regression Model
    ↓
Evaluation (Accuracy, Precision, Recall, F1, Confusion Matrix)
    ↓
Streamlit Web App Deployment
```

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/titanic-survival-predictor.git

# 2. Go to project folder
cd titanic-survival-predictor

# 3. Install requirements
pip install -r requirements.txt

# 4. Run the app
python -m streamlit run titanic.py
```

---

## 📁 Project Structure

```
titanic-survival-predictor/
│
├── titanic.py                  # Streamlit web application
├── titanic_survival.ipynb      # Full ML pipeline notebook
├── titanic_model.pkl           # Saved trained model
├── titanic_scaler.pkl          # Saved StandardScaler
├── titanic.csv                 # Dataset
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation
```

---

## 💡 Key Learnings

- Logistic Regression is perfect for binary classification problems
- Label Encoding is essential before feeding categorical data to ML models
- StandardScaler improves Logistic Regression performance significantly
- Precision vs Recall trade-off depends on the business context
- Confusion Matrix gives much deeper insight than accuracy alone

---

## 👤 Author

**Pratik Mishra**
- 📧 pratikmisha141@gmail.com
- 🔗 [LinkedIn](https://linkedin.com/in/pratik-mishra)
- 🐙 [GitHub](https://github.com/your-username)

---

⭐ If you found this project useful, please give it a star!
