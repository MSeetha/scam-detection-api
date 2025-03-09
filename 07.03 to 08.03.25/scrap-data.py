import instaloader
import pandas as pd

# Initialize Instaloader
L = instaloader.Instaloader()

# Login (only needed for private accounts or more requests)
USERNAME = "seetha_manogaran"
PASSWORD = "your_instagram_password"
L.load_session_from_file(USERNAME)  # Load session if already logged in
# L.login(USERNAME, PASSWORD)  # Uncomment if logging in manually

# Define the hashtag to scrape
hashtag = "scamalert"  # Change this to any hashtag you want

# List to store post data
data = []

# Scrape posts under the hashtag
for post in instaloader.Hashtag.from_name(L.context, hashtag).get_posts():
    post_data = {
        "username": post.owner_username,
        "post_url": f"https://www.instagram.com/p/{post.shortcode}/",
        "caption": post.caption if post.caption else "",
        "likes": post.likes,
        "comments": post.comments,
        "date": post.date.strftime("%Y-%m-%d %H:%M:%S")
    }
    data.append(post_data)

    # Stop after scraping 100 posts (Modify as needed)
    if len(data) >= 100:
        break

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("dataset.csv", index=False, encoding="utf-8")

print("Data saved to dataset.csv")
