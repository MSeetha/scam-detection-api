import pandas as pd

# Load the cleaned data from the CSV file (Ensure that the path is correct)
df = pd.read_csv("instagram_data_with_scam_score.csv")  # Update with your actual file path

# Check if the "Caption" column exists
if "Caption" not in df.columns:
    print("Error: 'Caption' column is missing from the CSV file.")
else:
    # Apply a lambda function to classify captions as scam or not
    df["Label"] = df["Caption"].apply(lambda x: 1 if isinstance(x, str) and "scam" in x.lower() else 0)

    # Save the updated DataFrame with labels to a new CSV file
    df.to_csv("instagram_data_with_labels.csv", index=False)

    # Print the first few rows to verify the results
    print(df.head())

