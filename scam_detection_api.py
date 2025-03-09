from fastapi import FastAPI
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()

# Load the trained model and vectorizer
model = joblib.load("C:\\Users\\Asus\\AppData\\Local\\Instaloader\\scam_detection_model.pkl")
vectorizer = joblib.load("C:\\Users\\Asus\\AppData\\Local\\Instaloader\\tfidf_vectorizer.pkl")

@app.post("/predict/")
async def predict_scam(text: str):
    # Transform input text using the fitted vectorizer
    text_vectorized = vectorizer.transform([text])

    # Make prediction
    prediction = model.predict(text_vectorized)

    # Return Scam/Not Scam result
    result = "Scam" if prediction[0] == 1 else "Not Scam"
    return {"input_text": text, "prediction": result}

print("API is ready. Visit http://127.0.0.1:8000/docs to test.")
