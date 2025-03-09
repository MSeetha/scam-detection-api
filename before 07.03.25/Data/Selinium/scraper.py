from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Define Instagram login credentials
USERNAME = "seetha_manogaran"
PASSWORD = "Yashnevathy"

# Define hashtags for scraping
hashtags = [
    "scamalert", "fraudalert", "scammer", "bewareofscams", "dontgetsued", 
    "fakeaccount", "reportscams", "stopfraud", "onlinescam", "socialmediascam",
    "phishingscam", "identitytheft", "databreach", "cyberfraud", "phishingalert",
    "fakeemail", "fakelink", "scamwebsite", "clickbaitscam", "malwareattack",
    "bankfraud", "creditcardfraud", "fakeinvestment", "investmentfraud", "forexscam",
    "binaryoptionscam", "ponzischeme", "loanscam", "moneylaundering", "fakecheque",
    "onlineshoppingfraud", "fakestore", "counterfeitgoods", "fakeproducts", 
    "dropshipscam", "resalescam", "refundfraud", "paypalscam", "stolencreditcard",
    "giveawayscam", "fakelottery", "fakecontest", "sweepstakescam", "lotteryfraud",
    "prizescam", "claimyourprize", "youvewonascam", "jobscam", "fakejoboffer",
    "workfromhomescam", "mlmscam", "pyramidscheme", "remotejobfraud", "unpaidinternshipscam",
    "romancescam", "catfishscam", "onlinedatingscam", "fakeprofile", "lovescammer",
    "sugardaddyscam", "datingfraud", "techsupportscam", "microsoftscam", "appleidscam",
    "fakecustomerhelp", "helpdeskscam", "malwarewarning", "cryptoscam", "bitcoinfraud",
    "nftscam", "fakeairdrops", "faketokens", "rugpullscam", "pumpanddump"
]

# Initialize Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Open browser in full screen
driver = webdriver.Chrome(options=options)

# Login to Instagram
def login():
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)
    
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(10)

# Scrape posts from a hashtag
def scrape_hashtag(hashtag):
    driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    time.sleep(5)
    
    post_links = set()
    
    for _ in range(3):  # Scroll to load more posts
        posts = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")
        for post in posts:
            post_links.add(post.get_attribute("href"))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    return list(post_links)

# Scrape captions and comments
def scrape_post(post_url):
    driver.get(post_url)
    time.sleep(3)
    
    try:
        caption_element = driver.find_element(By.XPATH, "//span[contains(@class, '_aacl')]")
        caption = caption_element.text if caption_element else "No caption"
    except:
        caption = "No caption"

    comments = []
    try:
        comment_elements = driver.find_elements(By.XPATH, "//ul[contains(@class, '_a9z6')]/div/li/div/div/div/span")
        comments = [comment.text for comment in comment_elements]
    except:
        comments = []

    return {"url": post_url, "caption": caption, "comments": comments}  # ✅ Now correctly inside the function

# Scrape Direct Messages (DMs)
def scrape_dms():
    driver.get("https://www.instagram.com/direct/inbox/")
    time.sleep(5)
    
    messages = []
    try:
        chats = driver.find_elements(By.XPATH, "//div[contains(@class, '_ab8w')]")
        for chat in chats[:20]:  # Limit to 20 recent chats
            chat.click()
            time.sleep(3)
            
            msg_elements = driver.find_elements(By.XPATH, "//div[contains(@class, '_aacl')]")
            for msg in msg_elements:
                messages.append(msg.text)
    except:
        pass
    
    return messages

# Main Function
login()
all_data = []

for hashtag in hashtags:
    print(f"Scraping posts for #{hashtag}...")
    post_urls = scrape_hashtag(hashtag)

    for post_url in post_urls[:5]:  # Limit to 5 posts per hashtag
        data = scrape_post(post_url)
        if data:  # Only add if data is not None
            all_data.append(data)

# Scrape DMs
dm_data = scrape_dms()
for dm in dm_data:
    all_data.append({"url": "DM", "caption": "DM", "comments": dm})

# Save Data to CSV
df = pd.DataFrame(all_data)  # ✅ Fixed issue where 'data' was used instead of 'all_data'
df.to_csv("instagram_dataset.csv", index=False, encoding="utf-8")
print("✅ Data saved successfully!")

driver.quit()
