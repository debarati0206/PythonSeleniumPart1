from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjFormSubmission.HomePage import Homepage
from utilitiesHomePage.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        #creating object of HomePage
        homepage = Homepage(self.driver)
        homepage.getName().send_keys("Debarati")
        # driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Automation Engineer") #name
        time.sleep(2)
        homepage.getEmail().send_keys("demo@gmail.com")
        # driver.find_element(By.NAME,"email").send_keys("demo@gmail.com") #email
        time.sleep(2)
        homepage.getPwd().send_keys("demopwd")
        # driver.find_element(By.ID,"exampleInputPassword1").send_keys("demopassword")
        time.sleep(2)
        homepage.getChkbox().click()
        # driver.find_element(By.XPATH,"//*[@id='exampleCheck1']").click() #checkbox
        time.sleep(2)
        self.selectGender(homepage.selectDrpdwn(),"Female") #selectGender(self,locator, text)
        # dropdown.select_by_index(0)
        time.sleep(3)
        homepage.clickSubmit().click() #submit
        time.sleep(3)
        message_displayed = homepage.disp_Msg().text
# assert "Successor" in message_displayed

        if "Success" in message_displayed:
            print("form submitted successfully")
        else:
            print("error found")
        time.sleep(2)
        homepage.data_BindingMsg().send_keys("Python Automation Engineer")
        time.sleep(2)
        homepage.data_BindingMsg().clear()
        time.sleep(5)









