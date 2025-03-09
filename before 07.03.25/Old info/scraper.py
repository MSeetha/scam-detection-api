import snscrape.modules.twitter as sntwitter
import pandas as pd

# Define search query
query = "scam OR fraud OR phishing since:2024-01-01 until:2025-02-25 lang:en"

# Scrape tweets
tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    tweets.append([tweet.date, tweet.user.username, tweet.content, tweet.url])
    if i >= 100:  # Limit to 100 tweets
        break

# Convert to DataFrame & Save
df = pd.DataFrame(tweets, columns=["Date", "Username", "Tweet", "URL"])
df.to_csv("dataset_twitter.csv", index=False)

print("Saved to dataset_twitter.csv")
