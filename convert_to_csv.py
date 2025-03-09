import os
import json
import pandas as pd

# Define the root folder where data is stored
root_folder = r"C:\Users\Asus\AppData\Local\Instaloader\Data"

# List to store extracted data
data_list = []

# Loop through each folder inside the root directory
for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)

    # Check if it is a folder
    if os.path.isdir(folder_path):
        json_file = os.path.join(folder_path, "UTC.json")  # Change file name if needed

        # Check if JSON file exists in the folder
        if os.path.exists(json_file):
            with open(json_file, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)  # Load JSON data
                    
                    for post in data:
                        data_list.append({
                            "Post ID": post.get("id", ""),
                            "Username": post.get("owner", {}).get("username", ""),
                            "Caption": post.get("caption", ""),
                            "Likes": post.get("likes", ""),
                            "Comments Count": post.get("comments_count", ""),
                            "Post URL": post.get("shortcode", ""),
                        })
                except json.JSONDecodeError:
                    print(f"Error decoding JSON in {json_file}")

# Convert extracted data into a DataFrame
df = pd.DataFrame(data_list)

# Save to CSV file
csv_path = os.path.join(root_folder, "instagram_data.csv")
df.to_csv(csv_path, index=False, encoding="utf-8")

print(f"✅ Data saved successfully to {csv_path}")
