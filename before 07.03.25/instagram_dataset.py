import instaloader
import pandas as pd

# Initialize Instaloader
L = instaloader.Instaloader()

# Login to Instagram
USERNAME = "fulltime_troublemaker"
PASSWORD = "Yashnevathy"  # Replace with App Password if needed

try:
    L.login(USERNAME, PASSWORD)
    print("✅ Login successful!")
except Exception as e:
    print(f"❌ Login failed: {e}")
    exit()

# Define hashtags to scrape
hashtag = [
"scamalert"
] # Change this to any hashtag you want

# List to store post data
data = []

# Scrape posts under each hashtag
for tag in hashtag:
    print(f"🔍 Checking posts for: #{tag}")

    try:
        hashtag = instaloader.Hashtag.from_name(L.context, tag)
        count = 0  # Track the number of posts retrieved
        for post in hashtag.get_posts():
            print(f"📌 Found post: {post.owner_username}, {post.shortcode}")  # Print post details

            post_data = {
                "username": post.owner_username,
                "post_url": f"https://www.instagram.com/p/{post.shortcode}/",
                "caption": post.caption if post.caption else "",
                "likes": post.likes,
                "comments": post.comments,
                "date": post.date.strftime("%Y-%m-%d %H:%M:%S"),
                "hashtag": tag
            }
            data.append(post_data)
            count += 1

            if count >= 10:  # Limit to 10 posts for testing
                break

        print(f"✅ {count} posts found for #{tag}")
    except Exception as e:
        print(f"⚠️ Error scraping #{tag}: {e}")

    
    # Stop after scraping 500 posts (to prevent getting blocked)
    if len(data) >= 500:
        break

# Convert to DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv("instagram_dataset.csv", index=False, encoding="utf-8")

print("✅ Data saved to instagram_dataset.csv")

