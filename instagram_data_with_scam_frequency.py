import pandas as pd

# Load the CSV file
file_path = "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\instagram_data_with_label.csv"
df = pd.read_csv(file_path, header=0)  # Ensure first row is treated as headers

# Print all column names to verify
print("Column Names in CSV:", df.columns.tolist())  

# Define common scam-related keywords
scam_keywords = ["scam", "fraud", "giveaway", "winner", "congratulations", "limited offer", 
                 "claim now", "click link", "urgent", "lottery", "prize", "free", "discount", 
                 "money", "transfer", "pay now", "risk-free", "exclusive deal"]

# Function to count scam-related words in a text
def scam_word_frequency(text):
    if isinstance(text, str):  # Ensure it's a string before processing
        return sum(text.lower().count(word) for word in scam_keywords)
    return 0  # Return 0 if the text is not valid

# Apply function to the correct column ("Caption")
df.columns = df.columns.str.strip()  # Remove extra spaces
df["Scam_Word_Frequency"] = df["Caption"].apply(scam_word_frequency)  

# Save the updated dataset
updated_file_path = "C:\\Users\\Asus\\AppData\\Local\\Instaloader\\instagram_data_with_scam_frequency.csv"
df.to_csv(updated_file_path, index=False)

print(f"Updated file saved at: {updated_file_path}")
