from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Set up Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)

# Instagram login credentials
USERNAME = "seetha_manogaran"
PASSWORD = "Yashnevathy"

# Open Instagram login page
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)  # Wait for the page to load

# Enter username
username_input = driver.find_element(By.NAME, "username")
username_input.send_keys(USERNAME)

# Enter password
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)

time.sleep(5)  # Wait for login to complete

# List of scam-related hashtags
hashtags = ["scamalert", "giveaway", "lottery", "phishingscam", "bankscam"]
data = []

# Function to wait for an element to be present
def wait_for_element(xpath, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))

for hashtag in hashtags:
    driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    time.sleep(5)

    # Find post links
    posts = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")
    post_links = [post.get_attribute("href") for post in posts[:10]]  # Scrape only 10 posts per hashtag

    for post_link in post_links:
        driver.get(post_link)
        time.sleep(5)

        try:
            # Wait for the caption to load
            wait_for_element("//div[contains(@class, '_a9zs')]")

            # Get post caption
            caption_element = driver.find_element(By.XPATH, "//div[contains(@class, '_a9zs')]/span")
            caption = caption_element.text if caption_element else "No caption"

            # Wait for comments to load
            wait_for_element("//span[contains(@class, '_a9zs')]")

            # Get comments
            comment_elements = driver.find_elements(By.XPATH, "//span[contains(@class, '_a9zs')]")
            comments = [comment.text for comment in comment_elements[1:]]  # Exclude first one (caption)
            comments = " | ".join(comments) if comments else "No comments"

            # Store the data
            data.append({"Hashtag": hashtag, "Post URL": post_link, "Caption": caption, "Comments": comments})
            print(f"Scraped: {post_link}")

        except Exception as e:
            print(f"Error scraping post {post_link}: {e}")

# Save data to CSV
df = pd.DataFrame(data)
df.to_csv("instagram_data.csv", index=False, encoding="utf-8")

print("✅ Data saved successfully to instagram_data.csv")

# Close the browser
driver.quit()
