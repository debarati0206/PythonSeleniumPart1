from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

obj = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=obj)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("Testing frame")
time.sleep(1)
driver.switch_to.default_content()
header = driver.find_element(By.TAG_NAME,'h3').text #it's outside frame
assert header == "An iFrame containing the TinyMCE WYSIWYG Editor"