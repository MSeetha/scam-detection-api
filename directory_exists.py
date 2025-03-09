import os

# Define the directory path
directory = r"C:\Users\Asus\AppData\Local\Instaloader\Data"

# Check if the directory exists
if os.path.exists(directory):
    print(f"✅ The directory exists: {directory}")
else:
    print(f"❌ The directory does not exist: {directory}")
