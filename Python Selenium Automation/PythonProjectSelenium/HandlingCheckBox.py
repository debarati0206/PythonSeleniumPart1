from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
obj = webdriver.EdgeOptions()
driver = webdriver.Edge(options=obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']") #all checkboxes option in checkboxes list
# checkboxes = driver.find_elements(By.CSS_SELECTOR," input[type='checkbox']") #all checkboxes option in checkboxes list
print(len(checkboxes))
for checkbox in checkboxes: #check every checkbox
        if checkbox.get_attribute('value') == 'option2':
                checkbox.click()
                time.sleep(3)
                if checkbox.is_displayed:
                        print("checkbox displayed")
                else:
                        print("not displayed")
                assert checkbox.is_selected()
                break
    # if checkbox.text == 'Option2': -- it'll not work .text as checkbox is dynamically selected

        
# radiobuttons = driver.find_elements(By.CSS_SELECTOR," input[type='radio']")
# for radiobutton in radiobuttons:
#         if radiobutton.get_attribute('value') == 'radio2':
#                 radiobutton.click()
#                 time.sleep(2)
#                 break
radiobuttonss = driver.find_elements(By.CSS_SELECTOR," input[type='radio']") #radiobuttons in list
radiobuttonss[2].click() #3rd indexed radio button is clicked
time.sleep(2)
assert driver.find_element(By.ID,"displayed-text").is_displayed() #hide/show textbox by clicking hide/show button
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
# print(driver.find_element(By.ID,"displayed-text").is_displayed())
# driver.find_element(By.ID,"hide-textbox").click()
# print(driver.find_element(By.ID,"displayed-text").is_displayed())

