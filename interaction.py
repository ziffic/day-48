from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import connect

# Connect to Chrome Browser
chrome_driver_path = Service(connect.CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_driver_path)

# site_url = "https://en.wikipedia.org/wiki/Main_Page"
# driver.get(site_url)

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# wikiversity = driver.find_element(By.LINK_TEXT, "Wikiversity")
# wikiversity.click()


# google_url = "https://www.google.com"
# driver.get(google_url)
#
# search = driver.find_element(By.NAME, "q")
# print(f"Search: {search.text}")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# Code Challenge
url = "https://web.archive.org/web/20220120120408/http://secure-retreat-92358.herokuapp.com/"
driver.get(url)

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Dave")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Smith")
email = driver.find_element(By.NAME, "email")
email.send_keys("test@test.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click()

while True:
    pass
