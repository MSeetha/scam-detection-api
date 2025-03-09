import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset with the label column
df = pd.read_csv("instagram_data_with_label.csv")

# Ensure necessary columns exist
required_columns = ["Scam_Score_Caption", "Label"]
for col in required_columns:
    if col not in df.columns:
        print(f"Error: '{col}' column is missing from the dataset.")
        exit()

# Dummy feature extraction (Replace with actual feature vectors)
X_caption = np.random.rand(len(df), 10)  

# Combine features with scam score
X = pd.concat([pd.DataFrame(X_caption), df[["Scam_Score_Caption"]]], axis=1)

# Convert all column names to strings
X.columns = X.columns.astype(str)  

# Target variable
y = df["Label"]

# Split data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Model evaluation
y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the trained model
joblib.dump(rf_model, "rf_model.pkl")
print("Model saved as 'rf_model.pkl'.")
