import streamlit as st
import pickle
import os
import numpy as np

# ----------------------------
# Step 1: Model path
# ----------------------------
MODEL_PATH = "heart_model.pkl"  # make sure this file is in the same folder

# ----------------------------
# Step 2: Load model safely
# ----------------------------
def load_model(path):
    if not os.path.exists(path):
        st.error(f"Model file not found at {path}")
        return None
    try:
        with open(path, "rb") as f:
            model = pickle.load(f)
        return model
    except ModuleNotFoundError as e:
        st.error(f"Module missing: {e}. Install it in requirements.txt.")
        return None
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model(MODEL_PATH)

# ----------------------------
# Step 3: Streamlit UI
# ----------------------------
st.title("💓 Heart Disease Prediction App")

if model:
    st.subheader("Enter your details:")

    # Example input fields (update based on your model features)
    age = st.number_input("Age", min_value=1, max_value=120, value=30)
    sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
    cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3, value=1)
    trestbps = st.number_input("Resting Blood Pressure", min_value=50, max_value=250, value=120)
    chol = st.number_input("Serum Cholesterol", min_value=100, max_value=600, value=200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (0 = No, 1 = Yes)", [0, 1])
    restecg = st.number_input("Resting ECG (0-2)", min_value=0, max_value=2, value=1)
    thalach = st.number_input("Max Heart Rate Achieved", min_value=50, max_value=250, value=150)
    exang = st.selectbox("Exercise Induced Angina (0 = No, 1 = Yes)", [0, 1])
    oldpeak = st.number_input("ST Depression induced by exercise", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    slope = st.number_input("Slope of ST segment (0-2)", min_value=0, max_value=2, value=1)
    ca = st.number_input("Number of major vessels (0-3) colored by fluoroscopy", min_value=0, max_value=3, value=0)
    thal = st.number_input("Thalassemia (1-3)", min_value=1, max_value=3, value=2)

    # Predict button
    if st.button("Predict"):
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                                thalach, exang, oldpeak, slope, ca, thal]])
        prediction = model.predict(input_data)
        st.success("Prediction: ✅ Heart Disease" if prediction[0] == 1 else "Prediction: ❌ No Heart Disease")
else:
    st.warning("Model not loaded. Check logs or model path.")



      
