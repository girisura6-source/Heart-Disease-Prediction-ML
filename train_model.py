import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
data = pd.read_csv("C:\python\Heart_Disease_Prediction\heart.csv")

# Features & Target
X = data.drop("target", axis=1)
Y = data["target"]

# Split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

# Accuracy
print("Training Accuracy:", accuracy_score(Y_train, model.predict(X_train)))
print("Testing Accuracy:", accuracy_score(Y_test, model.predict(X_test)))

# Save model
pickle.dump(model, open("heart_model.pkl", "wb"))

print("heart_model.pkl created successfully")
