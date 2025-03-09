import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the labeled dataset
file_path = "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\instagram_data_with_scam_label.csv"
df = pd.read_csv(file_path, header=0)

# Function to clean text
def clean_text(text):
    if isinstance(text, str):
        text = re.sub(r"http\S+", "", text)  # Remove URLs
        text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters
        text = text.lower()  # Convert to lowercase
        return text
    return ""

# Apply text cleaning
df["Cleaned_Text"] = df["Caption"].apply(clean_text)

# Convert text to numerical features using TF-IDF
vectorizer = TfidfVectorizer(max_features=500)
X = vectorizer.fit_transform(df["Cleaned_Text"])

# Save the cleaned dataset
df.to_csv("C:\\Users\\Asus\\AppData\\Local\\Instaloader\\processed_instagram_data.csv", index=False)
print("Preprocessing completed!")
