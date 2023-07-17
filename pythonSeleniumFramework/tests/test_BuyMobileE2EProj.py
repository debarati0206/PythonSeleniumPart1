import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Checkout import CheckOutPage
from pageObjects.Confirmation import ConfirmationPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    # def test_e2e(self,setup):
    #
    #     setup.find_element(By.XPATH ,"//a[contains(@href,'shop')]").click()
    def test_e2e(self):
        #creating object of HomePage
        homepage = HomePage(self.driver) #from BaseClass go to conftest.py and invoke driver
        homepage.shopMobile().click() #driver.find_element(*HomePage.shop) = driver.find_element((By.XPATH,"//a[contains(@href,'shop')]").click()
        checkOutPage = CheckOutPage(self.driver)
        products = checkOutPage.getMobileNames()
        for product in products:
            # print(product.text)
            prod = product.text
            print(prod)
            if prod == 'Blackberry':
                checkOutPage.AddMobile.click()
                time.sleep(5)
        # checkingOut = CheckOutPage(self.driver)
        checkOutPage.CheckOut().click()
        # finallyCheckout = CheckOutPage(self.driver)
        checkOutPage.FinalCheckOutMobile().click()
        time.sleep(2)
        confirmation = ConfirmationPage(self.driver)
        confirmation.getCountry().send_keys("ind")
        wait = WebDriverWait(self.driver ,10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT ,"India")))
        # countrySelected = ConfirmationPage(self.driver)
        confirmation.chooseCountry().click()
        confirmation.checkTerms().click()
        confirmation.PurchaseMobile().click()
        # self.driver.find_element(By.XPATH ,"//div[@class='checkbox checkbox-primary']").click()
        # self.driver.find_element(By.XPATH ,"//input[@value='Purchase']").click()
        alert = confirmation.CatchAlert().text
        print(alert)
        time.sleep(3)
