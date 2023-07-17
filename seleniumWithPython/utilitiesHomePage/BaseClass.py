import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    def selectGender(self,locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
