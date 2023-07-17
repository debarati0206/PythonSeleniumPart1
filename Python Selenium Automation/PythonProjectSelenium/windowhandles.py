from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

obj = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=obj)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(5)
action = ActionChains(driver)
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened = driver.window_handles #put all open windows in a list
driver.switch_to.window(windowsOpened[1]) #child window
print(driver.find_element(By.TAG_NAME,'h3').text)
driver.close()
driver.switch_to.window(windowsOpened[0]) #parent window
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text