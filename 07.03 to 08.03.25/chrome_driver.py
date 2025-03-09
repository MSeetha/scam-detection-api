from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify path correctly
service = Service(r"C:\Users\Asus\AppData\Local\Instaloader\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Instagram
driver.get("https://www.instagram.com/")

# Close browser
driver.quit()
