import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)

# Load model and scaler
import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'titanic_model.pkl'), 'rb') as f:
    model = pickle.load(f)
with open(os.path.join(BASE_DIR, 'titanic_scaler.pkl'), 'rb') as f:
    scaler = pickle.load(f)

# ── Title ──
st.title("🚢 Titanic Survival Predictor")
st.markdown("Built by **Pratik Mishra** | Logistic Regression Model")
st.markdown("---")

st.subheader("Enter Passenger Details")

col1, col2 = st.columns(2)

with col1:
    pclass   = st.selectbox("Passenger Class", [1, 2, 3],
                             format_func=lambda x:
                             f"{'1st' if x==1 else '2nd' if x==2 else '3rd'} Class")
    sex      = st.selectbox("Sex", ["Female", "Male"])
    age      = st.slider("Age", 1, 80, 25)
    sibsp    = st.number_input("Siblings / Spouse aboard", 0, 8, 0)

with col2:
    parch    = st.number_input("Parents / Children aboard", 0, 6, 0)
    fare     = st.number_input("Ticket Fare ($)", 0.0, 600.0, 30.0)
    embarked = st.selectbox("Port of Embarkation",
                            ["Cherbourg (C)", "Queenstown (Q)", "Southampton (S)"])

st.markdown("---")

if st.button("🔮 Predict Survival", use_container_width=True):
    sex_val      = 1 if sex == "Female" else 0
    embarked_val = {"Cherbourg (C)": 0,
                    "Queenstown (Q)": 1,
                    "Southampton (S)": 2}[embarked]

    input_data = pd.DataFrame({
        'Pclass'  : [pclass],
        'Sex'     : [sex_val],
        'Age'     : [age],
        'SibSp'   : [sibsp],
        'Parch'   : [parch],
        'Fare'    : [fare],
        'Embarked': [embarked_val]
    })

    input_scaled = scaler.transform(input_data)
    prediction   = model.predict(input_scaled)[0]
    probability  = model.predict_proba(input_scaled)[0]

    if prediction == 1:
        st.success(f"### ✅ This passenger would have SURVIVED!")
    else:
        st.error(f"### ❌ This passenger would NOT have survived.")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Survival Probability",
                  f"{probability[1] * 100:.1f}%")
    with col2:
        st.metric("Death Probability",
                  f"{probability[0] * 100:.1f}%")

st.markdown("---")
st.markdown("🔗 Connect with me on [LinkedIn](https://linkedin.com/in/pratik-mishra)")