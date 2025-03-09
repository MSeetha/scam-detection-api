import instaloader  # Make sure you have installed this module

L = instaloader.Instaloader()
max_posts = 100  # Set your limit
count = 0

for post in L.get_hashtag_posts("scam"):
    if count >= max_posts:
        break  # Stop after scraping 100 posts
    print(post.url)  # Print or process your scraped data
    count += 1
