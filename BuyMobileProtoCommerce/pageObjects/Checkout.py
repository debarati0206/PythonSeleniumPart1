from selenium.webdriver.common.by import By

from pageObjects.Confirmation import ConfirmationPage


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver #after this create object of CheckOutPage in actual test & pass driver as arguement as constructor here accepts driver as arguement

    MobileName = (By.XPATH ,"//div[@class='card h-100']/div/h4")

    def getMobileNames(self):
        return self.driver.find_elements(*CheckOutPage.MobileName)  #calling class variable by classname.variable_name -> * treats the particular variable as tuple & deserialises like below commented line
        # = driver.find_element(By.XPATH ,"//a[contains(@href,'shop')]")

    AddMobile = (By.XPATH ,"//div/button[contains(.,'Add')]")

    def getMobileInCart(self):
        return  self.driver.find_element(*CheckOutPage.AddMobile)

    GoToCheckout = (By.XPATH ,"//a[@class='nav-link btn btn-primary']")

    def CheckOut(self):
        return self.driver.find_element(*CheckOutPage.GoToCheckout)

    finalCheckOut = (By.XPATH ,"//button[@class='btn btn-success']")

    def FinalCheckOutMobile(self):
        self.driver.find_element(*CheckOutPage.finalCheckOut).click()
        confirmation = ConfirmationPage(self.driver)
        return confirmation



