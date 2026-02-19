import streamlit as st
import pickle
import os
import numpy as np

# ----------------------------
# Model path
# ----------------------------
MODEL_PATH = "heart_model.pkl"

# ----------------------------
# Load model safely
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
        st.error(f"Module missing: {e}. Add it to requirements.txt")
        return None
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model(MODEL_PATH)

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("💓 Heart Disease Prediction")

if model:
    st.subheader("Enter your health details:")

    # Only essential features for simplicity
    age = st.number_input("Age", 1, 120, 30)
    sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
    cp = st.number_input("Chest Pain Type (0-3)", 0, 3, 1)
    trestbps = st.number_input("Resting Blood Pressure", 50, 250, 120)
    chol = st.number_input("Serum Cholesterol", 100, 600, 200)
    thalach = st.number_input("Max Heart Rate Achieved", 50, 250, 150)
    exang = st.selectbox("Exercise Induced Angina (0 = No, 1 = Yes)", [0, 1])

    if st.button("Predict"):
        input_data = np.array([[age, sex, cp, trestbps, chol, thalach, exang]])
        try:
            prediction = model.predict(input_data)
            st.success("✅ Heart Disease" if prediction[0] == 1 else "❌ No Heart Disease")
        except Exception as e:
            st.error(f"Prediction error: {e}")

else:
    st.warning("Model not loaded. Check model path or logs.")

      
