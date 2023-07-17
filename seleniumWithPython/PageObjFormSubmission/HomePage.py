from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    pwd = (By.ID, "exampleInputPassword1")
    chkbx = (By.XPATH, "//*[@id='exampleCheck1']")
    drpdwn = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH,"/html/body/app-root/form-comp/div/form/input")
    msg_display = (By.CLASS_NAME,"alert-success")
    data_bindingExmpl = (By.XPATH,"/html/body/app-root/form-comp/div/h4/input")

    def getName(self):
        return self.driver.find_element(*Homepage.name)

    def getEmail(self):
        return self.driver.find_element(*Homepage.email)

    def getPwd(self):
        return self.driver.find_element(*Homepage.pwd)

    def getChkbox(self):
        return self.driver.find_element(*Homepage.chkbx)

    def selectDrpdwn(self):
        return self.driver.find_element(*Homepage.drpdwn)

    def clickSubmit(self):
        return self.driver.find_element(*Homepage.submit)

    def disp_Msg(self):
        return self.driver.find_element(*Homepage.msg_display)

    def data_BindingMsg(self):
        return self.driver.find_element(*Homepage.data_bindingExmpl)
