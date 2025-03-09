profiles = ["cybercrimewatch", "fraudwatch", "scam_alerts"]  # Replace with actual scam-related pages

for username in profiles:
    print(f"🔍 Scraping posts from: @{username}")

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        count = 0
        for post in profile.get_posts():
            print(f"📌 Found post: {post.shortcode}, URL: https://www.instagram.com/p/{post.shortcode}/")
            count += 1
            if count >= 10:  # Limit for testing
                break
    except Exception as e:
        print(f"⚠️ Error scraping @{username}: {e}")
