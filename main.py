from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import connect

# Connect to Chrome Browser
chrome_driver_path = Service(connect.CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_driver_path)

# Find by class name
# driver.get("https://www.amazon.com")
# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_1_sspa?keywords=instant%2Bpot&qid=1681947277&sprefix=instant%2Caps%2C176&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzSTc1UkM0Nk05QTVJJmVuY3J5cHRlZElkPUEwODQyMDMxMlpSVVIyNlRERUVNSiZlbmNyeXB0ZWRBZElkPUEwNjg1MTEzMTRBUDJSNUxDVTZIQSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1")
# price = driver.find_element(By.CLASS_NAME, "a-offscreen").get_attribute("textContent")
# print(price)

# Find by name
driver.get("https://www.python.org")
# search_bar = driver.find_element(By.NAME, "q").tag_name
# print(search_bar)

# Find by class name
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# Find by css selector
# doc_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(doc_link.text)

# Find by xpath
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# Code Challenge
xpath = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/'
event_dates = [time.text for time in driver.find_elements(By.XPATH, f"{xpath}time")]
events_names = [event.text for event in driver.find_elements(By.XPATH, f"{xpath}a")]

print(event_dates[0])
print(events_names[0])
events = {}
for n in range(len(event_dates)):
    events[n] = {
        "time": f"2023-{event_dates[n]}",
        "name": events_names[n]
    }

print(events)

driver.close()
