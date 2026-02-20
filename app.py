# app.py
import streamlit as st
import pickle
import os
import numpy as np

<<<<<<< HEAD
# ----------------------------
# Step 1: Define the model path
# ----------------------------
MODEL_PATH = "heart_model.pkl"  # Make sure this file is in the same folder as app.py
=======
# Load model
import os
import pickle

model_path = os.path.join(os.getcwd(), "heart_model.pkl")
model = pickle.load(open(model_path, "rb"))
>>>>>>> 85b462088c2cb7502550e5c373c530919dd9866c

# ----------------------------
# Step 2: Load the model safely
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
# Step 3: Streamlit UI
# ----------------------------
st.title("💓 Heart Disease Prediction App")

if model:
    st.subheader("Enter your health details:")

    # ----------------------------
    # Simplified input fields
    # ----------------------------
    age = st.number_input("Age", 1, 120, 30)
    sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
    cp = st.number_input("Chest Pain Type (0-3)", 0, 3, 1)
    trestbps = st.number_input("Resting Blood Pressure", 50, 250, 120)
    chol = st.number_input("Serum Cholesterol", 100, 600, 200)
    thalach = st.number_input("Max Heart Rate Achieved", 50, 250, 150)
    exang = st.selectbox("Exercise Induced Angina (0 = No, 1 = Yes)", [0, 1])

    # ----------------------------
    # Predict button
    # ----------------------------
    if st.button("Predict"):
        # Prepare input as 2D array for model
        input_data = np.array([[age, sex, cp, trestbps, chol, thalach, exang]])
        try:
            prediction = model.predict(input_data)
            if prediction[0] == 1:
                st.success("✅ Prediction: Heart Disease")
            else:
                st.success("❌ Prediction: No Heart Disease")
        except Exception as e:
            st.error(f"Prediction error: {e}")

else:
    st.warning("Model not loaded. Check model path or logs.")


      
