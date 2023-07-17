# from selenium import webdriver
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.select import Select


# import time

# obj = webdriver.EdgeOptions()
# driver = webdriver.Edge(options=obj)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

obj = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5) #max wait for all element is 5 sec.
driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("ber")
time.sleep(2) #to make sure list includes all the 3 items not the empty list
options = driver.find_elements(By.XPATH,"//div[@class='products']/div ")
print(len(options))
assert len(options) > 0 # make sure the result list contains more than 0 element after search
pro_list = []
for option in options:
    option.find_element(By.XPATH,"div/button").click() # for each item click 'add to cart'
    pro_list.append(option.find_element(By.XPATH,"h4").text) # fetch item name by chaining from parent to child= //div[@class='products']/div/h4 to go to the product name
    # time.sleep(1)

print("{} {}".format("Product list printing by chaining from parent element ", pro_list))
#validate expected list and products list that appeared after search
products_list = []
products_name= driver.find_elements(By.XPATH,"//div/div/h4")
for product_name in products_name:
        products_list.append(product_name.text)
print(products_list)
expected_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
assert products_list == expected_list



driver.find_element(By.XPATH,"//img[@alt='Cart']").click() #cart
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click() #proceed to checkout
time.sleep(1)
#price sum validation
total_price = driver.find_elements(By.XPATH,"//td[5]/p[@class='amount']") #sum all items' total
sum =0
for price in total_price:
    sum = sum + int(price.text)
total_Amt = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
if sum ==  total_Amt:
    print("price validated successfully")

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy") #enter promo code
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click() #apply ---this can take more than 5 sec which is defined in implicit wait.For this we can't increase implicit time as this is the only case where more time will be taken.all other case will take max 5 sec. so use explicit wait.
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'.promoInfo'))) #wait until code applied is visible
time.sleep(1)
print(driver.find_element(By.CSS_SELECTOR,'.promoInfo').text) # code applied/empty/invalid code
discount_price = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert discount_price < total_Amt
print(discount_price)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click() #place order
time.sleep(1)
dropdown = Select(driver.find_element(By.XPATH,"//select[@style='width: 200px;']")).select_by_visible_text("India") #select country
time.sleep(2)
driver.find_element(By.XPATH,"//input[@class='chkAgree']").click() # agree terms and conditions
driver.find_element(By.XPATH,"//button[text()='Proceed']").click() # finally place order
time.sleep(2)