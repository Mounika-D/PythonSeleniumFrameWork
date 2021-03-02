from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self,driver):
        self.driver = driver
    shop = (By.LINK_TEXT , "Shop")
    name = (By.CSS_SELECTOR , "input[name='name']")
    email = (By.NAME , "email")
    password = (By.CSS_SELECTOR , "#exampleInputPassword1")
    checkbox = (By.ID , "exampleCheck1")
    dropdown = (By.ID , "exampleFormControlSelect1")
    submit = (By.XPATH , "//input[@type='submit']")
    message = (By.XPATH , "//*[contains(@class,'alert-success')]")



    def shopItems(self):
        #return self.driver.find_element(*HomePage.shop) #shop is class variable , so we have to call class variable as className.variable
                                                 # and star is because to deseriaize tuple items
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    def getPassword(self):
        return self.driver.find_element(*HomePage.password)
    def clickCheckBox(self):
        return self.driver.find_element(*HomePage.checkbox)
    def getGender(self):
        return self.driver.find_element(*HomePage.dropdown)
    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)
    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.message)