from selenium import webdriver
from selenium.webdriver.common.by import By
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
text = driver.find_element(By.CSS_SELECTOR,".im-para.red").text
# get email as list using regex
email_list = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)

# get email using split method - Please email us (at) mentor@rahulshettyacademy.com with below templ(at)e to receive response
'''    Please email us(0)  mentor@rahulshettyacademy.com with below templ(1)  - text.split('at')[1]
mentor@rahulshettyacademy.com with below templ-   text.split('at')[1].strip()
mentor@rahulshettyacademy.com-(0)       with below templ(1)    '''
                                 
emaill = text.split('at')[1].strip().split(" ")[0] #entor@rahulshettyacademy.com
print(emaill)
email = ' '.join([str(elem) for elem in email_list])
print(email)
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.XPATH,"//input[@id='username']").send_keys(email)
driver.find_element(By.ID,"password").send_keys("password")


driver.find_element(By.XPATH,"//select//option[@value='teach']").click()
# dropdown.select_by_value("teach")
driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()
alert =  driver.find_element(By.XPATH,"//div[@style='display: block;']").text
print(alert)
time.sleep(2)
