import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

obj = webdriver.EdgeOptions()
driver = webdriver.Edge(options=obj)
driver.get("https://www.makemytrip.com/")
driver.find_element(By.ID,"fromCity").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='From']").send_keys("del")
time.sleep(2)
cities =driver.find_elements(By.CSS_SELECTOR,"p[class*='blackText']")
print (len(cities))
for city in cities:
    if city.text =="Del Rio, United States":
        city.click()
        break


driver.find_element_by_xpath("//p[text()='Delhi, India']").click()



