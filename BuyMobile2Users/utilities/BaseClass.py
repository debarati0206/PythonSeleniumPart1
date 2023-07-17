import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggername = inspect.stack()[1][3] # Gets the name of the class / method from where this method is called i.e. test_editProfile in test_fixturesData.py
        logger = logging.getLogger(loggername)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  #filehandler object

        logger.setLevel(logging.DEBUG)
        return  logger

    def selectDropdownByText(self, locator, text):
        dropdown = Select(locator)  # homepage.selectDrpdwn() ->it's locator
        dropdown.select_by_visible_text(text)

    # creating cutom utilities using selenium
    def verifyCountryName(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))


