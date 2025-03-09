import pandas as pd

# Load dataset
df = pd.read_csv("instagram_data_with_scam_score.csv")

# Ensure 'Caption' column exists before proceeding
if "Caption" not in df.columns:
    print("Error: 'Caption' column is missing from the dataset.")
    exit()

# Generate labels based on scam-related words
def label_scam(caption):
    if isinstance(caption, str):
        scam_keywords = ["scam", "fraud", "fake", "phishing", "con", "spammer", "rm0"]
        return 1 if any(word in caption.lower() for word in scam_keywords) else 0
    return 0  # Default label for missing captions

df["Label"] = df["Caption"].apply(label_scam)

# Save the updated dataset
df.to_csv("instagram_data_with_label.csv", index=False)
print("Label column added and saved as 'instagram_data_with_label.csv'.")
