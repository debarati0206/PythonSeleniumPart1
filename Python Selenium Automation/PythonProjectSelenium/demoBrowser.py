from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time


obj  = webdriver.EdgeOptions()
driver2 = webdriver.Edge(options= obj)

driver2.get("https://www.w3schools.com/python/")
driver2.maximize_window()
time.sleep(3)
print(driver2.title)
print(driver2.current_url)
driver2.get("https://www.w3schools.com/python/python_classes.asp")
driver2.minimize_window()
driver2.maximize_window()
time.sleep(2)
driver2.back()
time.sleep(2)
driver2.refresh()
time.sleep(2)
driver2.forward()
time.sleep(2)
driver2.close()

#chrome browser
'''from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\WebDrivers\ChromeDriver\chromedriver.exe")
driver = webdriver.Chrome(service_obj)
driver.get("https://www.w3schools.com/python/")
time.sleep(5)
print(driver.title)
print(driver.current_url)
driver.close()'''