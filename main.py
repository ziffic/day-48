from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import connect

chrome_driver_path = Service(connect.CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.amazon.com")
