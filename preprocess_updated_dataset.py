import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the updated dataset
df = pd.read_csv("instagram_scams.csv")  # Ensure this file exists

# Check column names and preview data
print("Columns in dataset:", df.columns)
print(df.head())

# Fill missing values in 'Cleaned_Text' column
df["Cleaned_Text"] = df["Cleaned_Text"].fillna("")

# Feature extraction
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df["Cleaned_Text"]).toarray()  # Ensure correct column name

# Encode labels (Replace "label_column" with the actual column name)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df["Scam_Detection"])  # Update "Scam" if needed

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("✅ Data preprocessing completed!")

