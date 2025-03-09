import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# 🔹 **Step 1: Load the Updated Dataset**
df = pd.read_csv("instagram_scams.csv")  # Ensure the file path is correct

# 🔹 **Step 2: Load the Preprocessing Objects**
vectorizer = TfidfVectorizer(max_features=5000)
label_encoder = LabelEncoder()

# 🔹 **Step 3: Extract Features**
X = vectorizer.fit_transform(df["Cleaned_Text"].fillna("")).toarray()

# 🔹 **Step 4: Identify the Correct Label Column**
if "Scam_Detection" in df.columns:
    label_column = "Scam_Detection"
elif "Label" in df.columns:
    label_column = "Label"
else:
    raise ValueError("No valid label column found. Check dataset!")

# Encode labels
y = label_encoder.fit_transform(df[label_column])

# 🔹 **Step 5: Split Data**
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔹 **Step 6: Train Model**
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 🔹 **Step 7: Evaluate Model**
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy:.2f}")

# 🔹 **Step 8: Save the Model and Preprocessing Objects**
joblib.dump(model, "scam_detection_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

print("🎉 Model retraining completed and saved successfully!")

