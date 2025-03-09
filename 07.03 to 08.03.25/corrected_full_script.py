import instaloader  # ✅ Import the module

# Initialize Instaloader
L = instaloader.Instaloader()

# Login (Try loading session, otherwise log in manually)
username = "fulltime_troublemaker"
password = "Yashnevathy"

try:
    L.load_session_from_file(username)  # Load saved session
    print("✅ Session loaded successfully!")
except FileNotFoundError:
    print("🔑 Logging in...")
    L.login(username, password)  # Login if session is missing
    L.save_session_to_file()  # Save session for next time

# Profile-based scraping
profiles = ["cybercrimewatch", "fraudwatch", "scam_alerts"]  # Replace with actual scam-related pages

for username in profiles:
    print(f"🔍 Scraping posts from: @{username}")

    try:
        profile = instaloader.Profile.from_username(L.context, username)  # ✅ Correct Instaloader usage
        count = 0
        for post in profile.get_posts():
            print(f"📌 Post: {post.shortcode} | URL: https://www.instagram.com/p/{post.shortcode}/")
            count += 1
            if count >= 10:  # Limit for testing
                break
    except Exception as e:
        print(f"⚠️ Error scraping @{username}: {e}")

print("✅ Scraping complete!")
