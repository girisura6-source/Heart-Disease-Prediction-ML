import numpy as np
import streamlit as st
import pickle

# Load model
model = pickle.load(open("heart_model.pkl", "rb"))

st.title("❤️ Heart Disease Prediction System")

# ----------- Input Fields ------------

age = st.number_input("Age", min_value=1, max_value=120, value=45)

sex = st.selectbox("Sex", ["Male", "Female"])
sex = 1 if sex == "Male" else 0

cp = st.selectbox("Chest Pain Type (0-3)", [0,1,2,3])

trestbps = st.number_input("Resting Blood Pressure", min_value=50, max_value=250)

chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600)

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes","No"])
fbs = 1 if fbs == "Yes" else 0

restecg = st.selectbox("Resting ECG Result (0,1,2)", [0,1,2])

thalach = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=250)

exang = st.selectbox("Exercise Induced Angina", ["Yes","No"])
exang = 1 if exang == "Yes" else 0

oldpeak = st.number_input("Oldpeak (ST depression)", format="%.1f")

slope = st.selectbox("Slope (0,1,2)", [0,1,2])

ca = st.selectbox("Number of Major Vessels (0-3)", [0,1,2,3])

thal = st.selectbox("Thalassemia (0=Normal,1=Fixed,2=Reversible)", [0,1,2])

# -------- Prediction Button --------

if st.button("Predict Heart Disease"):
    input_data = np.array([
        age, sex, cp, trestbps, chol, fbs,
        restecg, thalach, exang, oldpeak,
        slope, ca, thal
    ]).reshape(1, -1)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Person has Heart Disease")
    else:
        st.success("✅ Person does NOT have Heart Disease")
      
