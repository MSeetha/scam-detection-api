import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
file_path = "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\instagram_data_with_scam_label.csv"
df = pd.read_csv(file_path, header=0)

# Print column names
print("Column Names in CSV:", df.columns.tolist())

# Check for missing values
print("Missing values in Label column:", df["Label"].isnull().sum())
print("Missing values in Most_Frequent_Keywords column:", df["Most_Frequent_Keywords"].isnull().sum())

# Fill missing text fields with "No keywords found" to avoid empty data
df["Most_Frequent_Keywords"] = df["Most_Frequent_Keywords"].fillna("")
df["Cleaned_Caption"] = df["Cleaned_Caption"].fillna("")

# Select the best column for text data
df["Text_Data"] = df["Most_Frequent_Keywords"].apply(lambda x: x if x.strip() != "" else df["Cleaned_Caption"])

# Drop NaN values from "Label" and "Text_Data"
df = df.dropna(subset=["Label", "Text_Data"])

# Convert "Label" column to numerical (Scam=1, Not Scam=0)
df["Label"] = df["Label"].map({"Scam": 1, "Not Scam": 0})
df = df.dropna(subset=["Label"])  # Drop any rows where mapping failed

# Remove empty values in "Text_Data"
df = df[df["Text_Data"].str.strip() != ""]

# If fewer than 100 rows remain, stop execution to avoid ML training failure
if df.shape[0] < 100:
    print(f"Error: Only {df.shape[0]} valid text rows remaining after filtering. Exiting script.")
    exit()

# Print sample text data
print("Sample text data:\n", df["Text_Data"].head(5))

# Convert text data into numerical format using TF-IDF
vectorizer = TfidfVectorizer(max_features=500)
X = vectorizer.fit_transform(df["Text_Data"])

# Define the target variable
y = df["Label"]

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save the updated dataset with predictions
df["Predicted_Label"] = model.predict(vectorizer.transform(df["Text_Data"]))
df["Predicted_Label"] = df["Predicted_Label"].map({1: "Scam", 0: "Not Scam"})

updated_file_path = "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\instagram_data_with_predictions.csv"
df.to_csv(updated_file_path, index=False)

print(f"Updated file saved at: {updated_file_path}")



