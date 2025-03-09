import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the cleaned data from the CSV file
df = pd.read_csv("instagram_data_cleaned_final.csv")  # Make sure the path is correct

# Fill NaN values in the 'Cleaned_Caption' column with empty strings
df["Cleaned_Caption"].fillna("", inplace=True)

# Initialize the TfidfVectorizer
vectorizer = TfidfVectorizer()

# Apply the vectorizer to the 'Cleaned_Caption' column and convert it to an array
X_caption = vectorizer.fit_transform(df["Cleaned_Caption"]).toarray()

# Print the shape of the resulting vector (number of documents x number of features)
print(f"Shape of vectorized captions: {X_caption.shape}")

# Optionally, you can print a few feature names (words) to inspect the vocabulary
print("Feature names (words) used in vectorization:")
print(vectorizer.get_feature_names_out()[:10])  # Print first 10 words


