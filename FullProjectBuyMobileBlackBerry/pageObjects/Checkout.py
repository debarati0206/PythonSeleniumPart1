from selenium.webdriver.common.by import By

from pageObjects.Confirmation import ConfirmationPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver  # after this create object of CheckOutPage in actual test & pass driver as arguement as constructor here accepts driver as arguement

    # MobileName = (By.XPATH ,"//div[@class='card h-100']/div/h4")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    GoToCheckout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    finalCheckOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def CheckOut(self):
        return self.driver.find_element(*CheckOutPage.GoToCheckout)

    def FinalCheckOutMobile(self):
        self.driver.find_element(*CheckOutPage.finalCheckOut).click()
        confirmation = ConfirmationPage(self.driver)
        return confirmation
