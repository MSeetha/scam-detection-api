import joblib
import pandas as pd

# Load the trained model
model = joblib.load("rf_model.pkl")

# Sample input (Replace with real data)
sample_data = pd.DataFrame([[0.5, 0.7, 0.3, 0.2, 0.8, 0.6, 0.1, 0.9, 0.4, 0.3, 1.2]], columns=[str(i) for i in range(10)] + ["Scam_Score_Caption"])

# Make a prediction
prediction = model.predict(sample_data)
print("Scam Prediction:", "Scam" if prediction[0] == 1 else "Not Scam")
