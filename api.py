from fastapi import FastAPI
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model
with open("rf_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Initialize FastAPI app
app = FastAPI()

@app.post("/predict/")
async def predict_scam(data: dict):
    caption = data["caption"]
    
    # Convert text into TF-IDF features (Make sure it matches training format)
    vectorizer = TfidfVectorizer()
    X_caption = vectorizer.fit_transform([caption]).toarray()

    # Predict using the trained model
    prediction = model.predict(X_caption)

    return {"prediction": "Scam" if prediction[0] == 1 else "Not Scam"}

