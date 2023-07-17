from selenium.webdriver.common.by import By


class ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver  # after this create object of ConfirmationPage in actual test & pass driver as arguement as constructor here accepts driver as arguement

    country = (By.XPATH, "//input[@id='country']")

    def getCountry(self):
        return self.driver.find_element(
            *ConfirmationPage.country)  # calling class variable by classname.variable_name -> * treats the particular variable as tuple & deserialises like below commented line

    selectCountry = (By.LINK_TEXT, "India")

    def chooseCountry(self):
        return self.driver.find_element(*ConfirmationPage.selectCountry)

    agreeTerms = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    def checkTerms(self):
        return self.driver.find_element(*ConfirmationPage.agreeTerms)

    purchase = (By.XPATH, "//input[@value='Purchase']")

    def PurchaseMobile(self):
        return self.driver.find_element(*ConfirmationPage.purchase)

    alertMsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def CatchAlert(self):
        return self.driver.find_element(*ConfirmationPage.alertMsg)
