from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver

    phoneText = (By.CSS_SELECTOR , "div[class='card-body'] h4")
    addButton = (By.CSS_SELECTOR , "button[class*=btn]")
    checkOut  = (By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']")
    def getPhonesText(self):
        return self.driver.find_elements(*CheckOutPage.phoneText)
    def addToCart(self):
        return self.driver.find_element(*CheckOutPage.addButton)
    def checkOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkOut)

        '''
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
        '''