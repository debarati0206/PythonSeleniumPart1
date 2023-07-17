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

    def test_e2e(self):
        #creating object of HomePage
        homepage = HomePage(self.driver)
        checkOutPage = homepage.shopMobile() #optimizing page object by putting the integration point page object in another page object. e.g. to go from homepage to shop need to click on shop, then only can go to checkout page, putting all these in homepage shopMobile()
        products = checkOutPage.getMobileNames()

        for product in products:
            prod = product.text
            print(prod)
            if prod == 'Blackberry':
                checkOutPage.getMobileInCart().click()
                time.sleep(2)
        checkOutPage.CheckOut().click()
        confirmation = checkOutPage.FinalCheckOutMobile()
        time.sleep(2)
        confirmation.getCountry().send_keys("ind")
        self.verifyCountryName("India")
        confirmation.chooseCountry().click()
        confirmation.checkTerms().click()
        confirmation.PurchaseMobile().click()
        alert = confirmation.CatchAlert().text
        print(alert)
        time.sleep(3)
