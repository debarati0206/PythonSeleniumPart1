import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self, getData):
        log = self.getLogger()
        # creating object of HomePage
        homepage = HomePage(self.driver)
        # log.info("Name is " + getData[0])
        log.info("Name is " + getData["name"])
        log.info("Email is " +getData["email"])
        #
        log.info("Password is " +getData["pwd"])
        log.info("Gender is " +getData["gender"])

        homepage.getName().send_keys(getData["name"])
        # homepage.getName().send_keys(TestAllData[0]) ->use this if we use tuple for testdata instead of dictionary
        homepage.getEmail().send_keys(getData["email"])
        homepage.getPwd().send_keys(getData["pwd"])
        homepage.getChkbox().click()
        '''dropdown = Select(homepage.selectDrpdwn()) #homepage.selectDrpdwn() ->it's locator
        dropdown.select_by_visible_text("Female")
        dropdown.select_by_index(0)'''

        self.selectDropdownByText(homepage.selectDrpdwn(), getData["gender"])
        time.sleep(2)
        homepage.clickSubmit().click()  # submit
        message_displayed = homepage.disp_Msg().text
        assert "Success" in message_displayed  # to set breakpoint click beside line no, a red bullet will appear, can see output in debug console and can resume from the particular breakpoint
        # homepage.data_BindingMsg().send_keys("Python Automation Engineer")
        # homepage.data_BindingMsg().clear()
        time.sleep(2)
        self.driver.refresh()  # to refresh the page after 1st testcase execution
        # time.sleep(2)

    # @pytest.fixture(params=[("Rahul","rs@gmail.com","rahulRS","Male"),("Anshikha","as@gmail.com","anshikaAS","Female")])  # this fixture is applied for only HomePage so creating here not in conftest.py
    # def getData(self, request):
    #     return request.param

    @pytest.fixture(
        params=HomePageData.test_HomePageData)  # this fixture is applied for only HomePage so creating here not in conftest.py
    def getData(self, request):
        return request.param
