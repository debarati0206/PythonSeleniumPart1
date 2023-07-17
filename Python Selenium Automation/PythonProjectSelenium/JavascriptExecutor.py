from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

obj = webdriver.ChromeOptions()
obj.add_argument("--start-maximized")
# obj.add_argument("headless")
obj.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=obj)

driver.get("https://rahulshettyacademy.com/documents-request")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
driver.get_screenshot_as_file("documents-request.png")
