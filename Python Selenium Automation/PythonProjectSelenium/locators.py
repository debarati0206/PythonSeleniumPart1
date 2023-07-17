from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

obj = webdriver.EdgeOptions()
driver = webdriver.Edge(options=obj)
#locators - NAME, ID, Xpath, CSSSelector, Classname,linkText
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Automation Engineer") #name
time.sleep(2)
driver.find_element(By.NAME,"email").send_keys("demo@gmail.com") #email
time.sleep(2)
driver.find_element(By.ID,"exampleInputPassword1").send_keys("demopassword")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='exampleCheck1']").click() #checkbox
time.sleep(2)

#static dropdown ----anything with select tag is static dropdown can use 'Select' there.
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/form/input").click() #submit
time.sleep(3)
message_displayed = driver.find_element(By.CLASS_NAME,"alert-success").text
# assert "Successor" in message_displayed

if "Success" in message_displayed:
    print("form submitted successfully")
else:
    print("error found")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/h4/input").send_keys("Python Automation Engineer")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/h4/input").clear()
time.sleep(5)





#xpath syntax = //tagname[@attribute = 'value'] -----e.g : //input[@type='submit']
#CSSSelector attribute = tagname[attribute = value] OR #idvalue OR .classname
#If element returns multiple elements then way to write css = (//tagname[@attribute='value])[occurance no]
                                                            # E.G - (//input[@type='text])[3] ----check the occurance by adding selectorshub extension in chrome and writing the css in that

