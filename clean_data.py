import pandas as pd
import re

# Load the data from the CSV file
df = pd.read_csv("instagram_data_cleaned.csv")  # Make sure the path is correct

# Define a function to clean text (remove unwanted characters, extra spaces, etc.)
def clean_text(text):
    if isinstance(text, str):  # Check if the text is a string
        text = text.lower()  # Convert to lowercase
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove non-alphanumeric characters (except spaces)
        text = re.sub(r"\s+", " ", text)  # Replace multiple spaces with a single space
        return text.strip()  # Remove leading/trailing spaces
    return text

# Apply the cleaning function to the 'Caption' column
df["Cleaned_Caption"] = df["Caption"].apply(clean_text)

# Save the cleaned data to a new CSV file
df.to_csv("instagram_data_cleaned_final.csv", index=False, encoding="utf-8")

print("Data has been cleaned and saved to 'instagram_data_cleaned_final.csv'")

