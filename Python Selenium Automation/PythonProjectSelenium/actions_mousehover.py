from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

obj = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# create action chain object
action = ActionChains(driver)
#for every action performed in ActionChains need to close by .perform()
# action.context_click(driver.find_element(By.XPATH,"//legend[text()='Mouse Hover Example']")) -- right click on 'Mouse Hover Example' 
# time.sleep(1)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform() # do hover on mousehover
time.sleep(3)
# action.move_to_element(driver.find_element(By.XPATH,"/html/body/div[4]/div/fieldset/div/div/a[1]")).click().perform() #from mousehover go to top and click
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform() #from mousehover go to reload and click
#Link text is applicable where there is ancor tag. <a> </a>
time.sleep(3) 
# action.double_click(driver.find_element(By.XPATH,"//input[@id='checkBoxOption2']"))
# time.sleep(3)