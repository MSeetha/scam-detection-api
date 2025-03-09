import pandas as pd

# Load the data
df = pd.read_csv("instagram_data.csv")  # Make sure the path to your CSV is correct

# Drop duplicates
df = df.drop_duplicates()

# Drop rows with missing captions 
df = df.dropna(subset=["Caption"])

# Save the cleaned data back to CSV
df.to_csv("instagram_data_cleaned.csv", index=False, encoding="utf-8")

# Print a message confirming the data was cleaned
print("Data cleaned and saved to 'instagram_data_cleaned.csv'")

