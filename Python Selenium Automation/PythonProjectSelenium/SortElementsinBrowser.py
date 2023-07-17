from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

obj = webdriver.ChromeOptions()
obj.add_argument("headless") 
driver = webdriver.Chrome(options=obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[.='Veg/fruit name']").click()
time.sleep(2)
item_list_webelements = driver.find_elements(By.XPATH,"//td[1]") #1st column
browserSortedlist = []
for item in item_list_webelements:
    print(item.text)
    browserSortedlist.append(item.text) #webelements to text
print(browserSortedlist)
browserSorted_listCopy = browserSortedlist.copy() #copy sorted list
print(browserSorted_listCopy)
browserSortedlist.sort() #sorting browser list through python
print(browserSortedlist) 
assert browserSorted_listCopy == browserSortedlist
