import pandas as pd

# Load the CSV file
file_path = "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\instagram_data_with_label.csv"
df = pd.read_csv(file_path, header=0)  # Ensure first row is treated as headers

# Print column names to verify the correct column name
print("Column Names in CSV:", df.columns.tolist())  

# Define common scam-related keywords
scam_keywords = ["scam", "fraud", "giveaway", "winner", "congratulations", "limited offer", 
                 "claim now", "click link", "urgent", "lottery", "prize", "free", "discount", 
                 "money", "transfer", "pay now", "risk-free", "exclusive deal"]

# Function to count scam-related words and extract frequently used ones
def scam_word_analysis(text):
    if isinstance(text, str):  # Ensure text is valid
        word_count = sum(text.lower().count(word) for word in scam_keywords)  # Count occurrences
        used_words = [word for word in scam_keywords if word in text.lower()]  # Extract found words
        return pd.Series([word_count, ", ".join(used_words)])  # Return both values
    return pd.Series([0, ""])  # Return 0 and empty string if invalid text

# Apply function to the "Caption" column
df.columns = df.columns.str.strip()  # Remove spaces from column names
df[["Scam_Word_Frequency", "Most_Frequent_Scam_Words"]] = df["Caption"].apply(scam_word_analysis)  

# Save the updated dataset
updated_file_path = "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\instagram_data_with_scam_frequency.csv"
df.to_csv(updated_file_path, index=False)

print(f"Updated file saved at: {updated_file_path}")
