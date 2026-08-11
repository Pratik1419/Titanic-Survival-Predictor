# Titanic-Survival-Predictor
A machine learning web application that predicts whether a Titanic passenger would have survived, using Logistic Regression. Built with Python, Scikit-learn, and deployed as an interactive Streamlit app.

🔗 Live App: Click here to try it
🐙 GitHub: View Source Code

📌 Project Overview

This project uses passenger data (age, class, sex, fare, etc.) to predict survival on the Titanic. A classic binary classification problem that demonstrates key ML concepts including data cleaning, encoding, scaling, model evaluation, and live deployment.

🎯 Problem Statement

Given passenger information, can we predict whether they would have survived the Titanic disaster?

0 = Did Not Survive ❌
1 = Survived ✅
📊 Dataset
Source: Kaggle — Titanic Dataset
Records: 891 passengers
Target Variable: Survived (0 or 1)
🔧 Features Used
Feature	Description
Pclass	Passenger class (1st, 2nd, 3rd)
Sex	Gender (Male / Female)
Age	Age of passenger
SibSp	Number of siblings / spouse aboard
Parch	Number of parents / children aboard
Fare	Ticket price paid
Embarked	Port of embarkation (C, Q, S)
🧹 Data Preprocessing Steps
✅ Filled missing Age values with median
✅ Filled missing Embarked values with mode
✅ Dropped Cabin column (too many missing values — 77%)
✅ Dropped Name, Ticket, PassengerId (not useful for prediction)
✅ Label Encoded Sex → (Male=0, Female=1)
✅ Label Encoded Embarked → (C=0, Q=1, S=2)
✅ Applied StandardScaler for feature normalization
🧪 Model Performance
Metric	Score
✅ Accuracy	82.03%
✅ Precision	80.73%
✅ Recall	76.86%
✅ F1 Score	Balanced between Precision & Recall

Industry benchmark for Titanic dataset: 78–85% accuracy.
This model achieves 82.03% — right in the strong range! 🎯

📊 Confusion Matrix Breakdown
	Predicted NOT Survived	Predicted Survived
Actually NOT Survived	True Negative ✅	False Positive ❌
Actually Survived	False Negative ❌	True Positive ✅
💡 Key Insights
Sex is the strongest predictor — females had much higher survival rates
Pclass is second most important — 1st class passengers survived more
Age matters — children had higher survival priority ("women and children first")
Fare correlates with class and therefore with survival rate
🛠️ Tech Stack
Tool	Purpose
Python	Core programming language
Pandas	Data cleaning & manipulation
NumPy	Numerical operations
Matplotlib & Seaborn	Data visualization
Scikit-learn	ML model, scaler, encoder, evaluation
Streamlit	Web application framework
Streamlit Cloud	Free deployment platform
Git & GitHub	Version control
🚀 How to Run Locally
bash
# 1. Clone the repository
git clone https://github.com/your-username/titanic-survival-predictor.git

# 2. Navigate into the folder
cd titanic-survival-predictor

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
python -m streamlit run titanic.py

App will open automatically at http://localhost:8501 🎉

📁 Project Structure
titanic-survival-predictor/
│
├── titanic.py                  # Streamlit web application
├── titanic_survival.ipynb      # Jupyter Notebook (full ML pipeline)
├── titanic_model.pkl           # Saved trained Logistic Regression model
├── titanic_scaler.pkl          # Saved StandardScaler
├── titanic.csv                 # Dataset
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
📦 requirements.txt
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
📈 What I Learned
Logistic Regression is ideal for binary classification problems
Feature encoding is essential before feeding categorical data into ML models
StandardScaler significantly improves Logistic Regression performance
Precision vs Recall trade-off depends on the business problem
Confusion Matrix gives deeper insight than accuracy score alone
Deploying ML models as web apps makes them accessible to everyone
🔮 Future Improvements
 Try Random Forest or XGBoost for higher accuracy
 Add feature importance chart in the app
 Add cross-validation for more robust evaluation
 Try hyperparameter tuning with GridSearchCV
👤 Author

Pratik Mishra
📧 pratikmisha141@gmail.com
🔗 LinkedIn
🐙 GitHub

⭐ If you found this project useful, please give it a star!
