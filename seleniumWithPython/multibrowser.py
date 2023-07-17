
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

driver.get('https://www.w3resource.com/java-exercises/oop/index.php')

time.sleep(10)
print(driver.title)
driver.close()

