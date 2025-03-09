import pandas as pd
from collections import Counter
import re

# Load the CSV file
file_path = "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\instagram_data_with_label.csv"
df = pd.read_csv(file_path, header=0)  # Ensure first row is treated as headers

# Print column names to verify the correct column name
print("Column Names in CSV:", df.columns.tolist())  

# Preprocess text: Remove special characters, split into words, and count frequency
all_words = []
df["Cleaned_Caption"] = df["Cleaned_Caption"].astype(str)  # Ensure text column is string

for text in df["Cleaned_Caption"]:
    words = re.findall(r'\b\w+\b', text.lower())  # Extract words, convert to lowercase
    all_words.extend(words)  # Add words to list

# Count word occurrences
word_counts = Counter(all_words)

# Get the **top 20 most frequent words** (adjust as needed)
most_frequent_words = [word for word, count in word_counts.most_common(20)]
print("Most Frequent Words:", most_frequent_words)

# Function to find frequently used words in each row
def find_frequent_words(text):
    words = re.findall(r'\b\w+\b', text.lower()) if isinstance(text, str) else []
    found_words = [word for word in words if word in most_frequent_words]
    return ", ".join(set(found_words))  # Remove duplicates and join

# Apply function to dataset
df["Most_Frequent_Keywords"] = df["Cleaned_Caption"].apply(find_frequent_words)

# Save the updated dataset
updated_file_path = "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\instagram_data_with_keywords.csv"
df.to_csv(updated_file_path, index=False)

print(f"Updated file saved at: {updated_file_path}")
