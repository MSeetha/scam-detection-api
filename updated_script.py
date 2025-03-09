import pandas as pd
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords (if not already installed)
nltk.download('stopwords')

# Load the CSV file
file_path = "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\instagram_data_with_label.csv"
df = pd.read_csv(file_path, header=0)  # Ensure first row is treated as headers

# Print column names to verify the correct column name
print("Column Names in CSV:", df.columns.tolist())  

# Convert "Cleaned_Caption" to string to prevent errors
df["Cleaned_Caption"] = df["Cleaned_Caption"].astype(str)

# Remove duplicate captions to keep only unique ones
df = df.drop_duplicates(subset=["Cleaned_Caption"], keep="first").reset_index(drop=True)

# Define stopwords to remove common words
stop_words = set(stopwords.words('english'))

# Preprocess text: Remove special characters, split into words, and count frequency
all_words = []
for text in df["Cleaned_Caption"]:
    words = re.findall(r'\b\w+\b', text.lower())  # Extract words, convert to lowercase
    filtered_words = [word for word in words if word not in stop_words]  # Remove stopwords
    all_words.extend(filtered_words)  # Add words to list

# Count word occurrences
word_counts = Counter(all_words)

# Get the **top 20 most frequent words** (excluding stopwords)
most_frequent_words = [word for word, count in word_counts.most_common(20)]
print("Most Frequent Words (Without Stopwords):", most_frequent_words)

# Function to find frequently used words in each row (excluding stopwords)
def find_frequent_words(text):
    words = re.findall(r'\b\w+\b', text.lower()) if isinstance(text, str) else []
    filtered_words = [word for word in words if word in most_frequent_words]
    return ", ".join(set(filtered_words))  # Remove duplicates and join

# Apply function to dataset
df["Most_Frequent_Keywords"] = df["Cleaned_Caption"].apply(find_frequent_words)

# Save the updated dataset
updated_file_path = "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\instagram_data_cleaned.csv"
df.to_csv(updated_file_path, index=False)

print(f"Updated file saved at: {updated_file_path}")
