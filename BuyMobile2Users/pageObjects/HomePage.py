from selenium.webdriver.common.by import By

from pageObjects.Checkout import CheckOutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver #after this create object of HomePage in actual test & pass driver as arguement as constructor here accepts driver as arguement

    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    pwd = (By.ID, "exampleInputPassword1")
    chkbx = (By.XPATH, "//*[@id='exampleCheck1']")
    drpdwn = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH,"/html/body/app-root/form-comp/div/form/input")
    msg_display = (By.CLASS_NAME,"alert-success")
    data_bindingExmpl = (By.XPATH,"/html/body/app-root/form-comp/div/h4/input")


    shop = (By.XPATH,"//a[contains(@href,'shop')]")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPwd(self):
        return self.driver.find_element(*HomePage.pwd)

    def getChkbox(self):
        return self.driver.find_element(*HomePage.chkbx)

    def selectDrpdwn(self):
        return self.driver.find_element(*HomePage.drpdwn)

    def clickSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def disp_Msg(self):
        return self.driver.find_element(*HomePage.msg_display)

    def data_BindingMsg(self):
        return self.driver.find_element(*HomePage.data_bindingExmpl)




    def shopMobile(self):
        self.driver.find_element(*HomePage.shop).click()  #calling class variable by classname.variable_name -> * treats the particular variable as tuple & deserialises like below commented line
        # = driver.find_element(By.XPATH ,"//a[contains(@href,'shop')]")
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
