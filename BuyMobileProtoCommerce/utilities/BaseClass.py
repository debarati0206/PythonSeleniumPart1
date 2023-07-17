import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    # creating cutom utilities using selenium
    def verifyCountryName(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectDropdownByText(self, locator, text):
        dropdown = Select(locator)  # homepage.selectDrpdwn() ->it's locator
        dropdown.select_by_visible_text(text)
