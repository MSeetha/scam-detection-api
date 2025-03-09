from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Path to your ChromeDriver (Update the path if needed)
chrome_driver_path = "C:\Users\Asus\AppData\Local\Instaloader\Data"  # Change this to your actual path
service = Service(chrome_driver_path)

# Open Chrome
driver = webdriver.Chrome(service=service)
driver.get("https://twitter.com/search?q=scam&f=live")

# Wait for page to load
time.sleep(5)

# Scroll down to load more tweets
for _ in range(3):  # Scroll 3 times
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(3)

# Collect tweets
tweets = driver.find_elements(By.CSS_SELECTOR, 'article div[lang]')
scam_texts = [tweet.text for tweet in tweets]

driver.quit()

print(scam_texts)  # Print the extracted tweets
