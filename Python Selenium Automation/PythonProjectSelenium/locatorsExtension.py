from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time 
from selenium.webdriver.common.by import By

obj = webdriver.EdgeOptions()
driver = webdriver.Edge(options=obj)
#locators - linkText
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"input[formcontrolname='userEmail']").send_keys("demo@gmail.com") # By.XPATH,"//form/div[1]/input" i.e. inside form in 1st div's input useremail is there
driver.find_element(By.CSS_SELECTOR,"input[formcontrolname='userPassword']").send_keys("demoPassword") # By.XPATH,"//form/div[2]/input" By.CSSSelector,"form div:nth-child(2) input"
driver.find_element(By.CSS_SELECTOR,"input[id='confirmPassword']").send_keys("demoPassword") #By.CSSSELECTOR,"#confirmPassword" i.e. #id value
driver.find_element(By.XPATH,"/html/body/app-root/app-password-new/div/div/div/div/div[2]/form/div[4]/button").click()
time.sleep(2)