from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver = driver #after this create object of HomePage in actual test & pass driver as arguement as constructor here accepts driver as arguement

    shop = (By.XPATH,"//a[contains(@href,'shop')]")

    def shopMobile(self):
        return self.driver.find_element(*HomePage.shop)  #calling class variable by classname.variable_name -> * treats the particular variable as tuple & deserialises like below commented line
        # = driver.find_element(By.XPATH ,"//a[contains(@href,'shop')]")

