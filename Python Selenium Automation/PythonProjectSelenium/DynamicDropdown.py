from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
obj = webdriver.EdgeOptions()
driver = webdriver.Edge(options=obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.ID,"autosuggest").send_keys("ind") # searching for country in the dynamic dropdown area
time.sleep(2)
# countries = driver.find_elements(By.XPATH,"//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all']//li") 
countries = driver.find_elements(By.CSS_SELECTOR, " li[class='ui-menu-item'] a") # "tagname[attribute = value] tag"-- it'll capture all the countries in a list which will appear after entering the send_keys("ind")  
print(len(countries))
# print(countries) #it'll return all the visible countries web element.
time.sleep(2)
for country in countries:
    if country.text == "Indonesia":
        print(country.text) #.text will give the value of country web element
        country.click()
        time.sleep(2)
        break



print(driver.find_element(By.ID,"autosuggest").get_attribute('value'))
# print(driver.find_element(By.ID,"autosuggest").text)
assert driver.find_element(By.ID,"autosuggest").get_attribute('value') =='Indonesia'