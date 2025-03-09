from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-blink-features=AutomationControlled") 
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Twitter (X) Search Page
url = "https://x.com/search?q=fraud&src=typed_query&f=live"
driver.get(url)

# Wait until tweets are visible
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, '//article//div[@data-testid="tweetText"]'))
)

# Find the posts (Inspect the page to find correct tags)
posts = driver.find_elements(By.XPATH, '//div[@dir="auto"]')

# Extract text from tweets
scam_posts = [post.text for post in posts]

# Close the browser
driver.quit()

# Print results
print(scam_posts)
