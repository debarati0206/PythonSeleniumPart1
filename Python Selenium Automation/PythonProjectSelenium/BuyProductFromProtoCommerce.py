from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

obj = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()
# driver.find_element(By.CSS_SELECTOR,"a[href*='hop']").click()
# products = driver.find_elements(By.XPATH,"//div[@class='card h-100/div/h4']")
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    # print(product.text)
    prod = product.find_element(By.XPATH,"div/h4").text
    # prod = product.text
    print(prod)
    if prod == 'Blackberry':
        product.find_element(By.XPATH,"div/button[contains(.,'Add')]").click()
        time.sleep(2)
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='country']").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()
alert = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
print(alert)
time.sleep(3)