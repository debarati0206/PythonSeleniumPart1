from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

obj = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=obj)
name = "deba"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID, "name").send_keys(name) #enter name in switch to alert box
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click() #click on alert button
time.sleep(1)
alert = driver.switch_to.alert # java popup appears- no html format-switch to alert
alertText = alert.text #grab alert text
print(alertText)
if name in alertText:
    print("name is taken as input in alertbox")
    time.sleep(2)