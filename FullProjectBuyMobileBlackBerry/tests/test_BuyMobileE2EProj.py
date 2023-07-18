# import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.Checkout import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.CheckOut().click()
        time.sleep(2)
        confirmation = checkOutPage.FinalCheckOutMobile()
        time.sleep(2)
        confirmation.getCountry().send_keys("ind")
        log.info("Searching for country india")
        self.verifyCountryName("India")
        confirmation.chooseCountry().click()
        confirmation.checkTerms().click()
        confirmation.PurchaseMobile().click()
        alert = confirmation.CatchAlert().text
        print(alert)
        log.info("Message displayed: "+alert)
        time.sleep(2)
        assert ("Success! Thank you!" in alert)












        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        # time.sleep(2)
        # confirmation = checkOutPage.FinalCheckOutMobile()
        # log.info("Entering country name as ind")
        # self.driver.find_element(By.ID, "country").send_keys("ind")
        # # time.sleep(5)
        # self.verifyLinkPresence("India")
        #
        # self.driver.find_element(By.LINK_TEXT, "India").click()
        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        # textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        # log.info("Text received from application is "+textMatch)

        # assert ("Success! Thank you!" in textMatch)
