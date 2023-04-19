from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import connect

chrome_driver_path = Service(connect.CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_driver_path)

# driver.get("https://www.amazon.com")
driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_1_sspa?keywords=instant%2Bpot&qid=1681947277&sprefix=instant%2Caps%2C176&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzSTc1UkM0Nk05QTVJJmVuY3J5cHRlZElkPUEwODQyMDMxMlpSVVIyNlRERUVNSiZlbmNyeXB0ZWRBZElkPUEwNjg1MTEzMTRBUDJSNUxDVTZIQSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1")
price = driver.find_element(By.CLASS_NAME, "a-offscreen").get_attribute("textContent")
print(price)
driver.close()
