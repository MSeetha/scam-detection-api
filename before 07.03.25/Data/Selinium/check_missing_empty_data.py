# Check for missing values
print(df.isnull().sum())

# Count empty captions
empty_captions = df[df['caption'].str.strip() == '']
print(f"Empty Captions: {len(empty_captions)}")

# Count empty comments
empty_comments = df[df['comments'] == '[]']
print(f"Empty Comments: {len(empty_comments)}")
