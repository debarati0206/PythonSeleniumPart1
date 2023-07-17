from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import re
import time
obj = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=obj)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
time.sleep(5)
text = driver.find_element(By.CSS_SELECTOR,".im-para.red").text
print(text)
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print(emails)
email = ' '.join([str(elem) for elem in emails])
print(email)
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.XPATH,"//input[@id='username']").send_keys(email)
driver.find_element(By.ID,"password").send_keys("password")
# driver.find_element(By.XPATH,"//input[@id='usertype']").click()

# radio_options= driver.find_elements(By.XPATH,"//span[@class='checkmark']")
# radio_options[1].click()
# driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()


driver.find_element(By.XPATH,"//select//option[@value='teach']").click()
# dropdown.select_by_value("teach")
driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()
alert =  driver.find_element(By.XPATH,"//div[@style='display: block;']").text
print(alert)
time.sleep(2)
