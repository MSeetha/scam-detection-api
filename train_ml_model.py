import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the cleaned dataset
file_path = "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\instagram_data_with_scam_label.csv"
df = pd.read_csv(file_path, header=0)

# Check if Scam_Detection column exists
if "Scam_Detection" not in df.columns:
    print("Error: 'Scam_Detection' column is missing in the dataset.")
    exit()

# Convert Scam_Detection column to numerical (Scam = 1, Not Scam = 0)
df["Label"] = df["Scam_Detection"].map({"Scam": 1, "Not Scam": 0})
df = df.dropna(subset=["Label", "Caption"])  # Remove missing values

# Convert text data into numerical features using TF-IDF
vectorizer = TfidfVectorizer(max_features=500)
X = vectorizer.fit_transform(df["Caption"])

# Define the target variable
y = df["Label"]

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model and vectorizer
joblib.dump(model, "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\scam_detection_model.pkl")
joblib.dump(vectorizer, "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\tfidf_vectorizer.pkl")

print("Model training completed and saved!")
