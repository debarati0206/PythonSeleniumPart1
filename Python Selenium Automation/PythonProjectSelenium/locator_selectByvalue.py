from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

obj = webdriver.EdgeOptions()
driver = webdriver.Edge(options=obj)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
dropdown = Select(driver.find_element(By.XPATH,"//*[@id='login-form']/div[5]/select/option[3]"))
dropdown.select_by_value('teach') #value is given in options so giving error
time.sleep(2)