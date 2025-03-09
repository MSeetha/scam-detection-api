import pandas as pd

# Load the cleaned data from the CSV file
df = pd.read_csv("instagram_data_cleaned_final.csv")  # Ensure the path is correct

# Define a list of scam-related keywords
scam_keywords = ["scam", "giveaway", "lottery", "winner", "prize", "fake", "phishing", "fraud"]

# Function to calculate a scam score based on the number of scam-related keywords in the caption
def scam_score(caption):
    # Check if the caption is a string (not NaN or other types)
    if isinstance(caption, str):
        # Convert the caption to lowercase for uniform comparison
        caption = caption.lower()
        # Count the number of scam keywords in the caption
        score = sum(keyword in caption for keyword in scam_keywords)
        return score
    else:
        # If caption is not a valid string, return a score of 0 (or any other default score)
        return 0

# Apply the scam_score function to the 'Cleaned_Caption' column
df["Scam_Score_Caption"] = df["Cleaned_Caption"].apply(scam_score)

# Save the updated DataFrame to a new CSV file
df.to_csv("instagram_data_with_scam_score.csv", index=False)

# Print out the first few rows to check the results
print(df.head())


