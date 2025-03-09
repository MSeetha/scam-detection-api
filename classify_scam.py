import pandas as pd

# Load the cleaned CSV file
file_path = "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\instagram_data_cleaned.csv"
df = pd.read_csv(file_path, header=0)

# Print column names to verify the correct column name
print("Column Names in CSV:", df.columns.tolist())

# Define scam-related words from "Most_Frequent_Keywords"
scam_indicators = ["turquoise", "cabsforsale", "please", "shipping", "first", "natural", "claim", "mine", "international", "turquoiseterritory", "giveaway", "one", "dm", "sale", "bestdeals", "scam", "coin", "australian"]

# Function to classify posts as Scam or Not Scam
def classify_scam(text):
    if isinstance(text, str):  # Ensure it's valid text
        for word in scam_indicators:
            if word in text.lower():
                return "Scam"
    return "Not Scam"

# Apply function to create Scam_Detection column
df["Scam_Detection"] = df["Most_Frequent_Keywords"].apply(classify_scam)

# Save the updated dataset
updated_file_path = "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\instagram_data_with_scam_label.csv"
df.to_csv(updated_file_path, index=False)

print(f"Updated file saved at: {updated_file_path}")
