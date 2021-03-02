from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.baseclass import BaseClass


class Testone(BaseClass):

    def test_e2e(self):
        self.driver.implicitly_wait(10)
        homepage = HomePage(self.driver)
        checkoutPage = homepage.shopItems()
        #homepage.shopItems().click() #commenting this as we can make code more optimized by reducing no. of objects in testcase
        #self.driver.find_element_by_link_text("Shop").click() (this can be optimized fpr 13,14 lines)
        #checkOutPage = CheckOutPage(self.driver)
        phones = checkoutPage.getPhonesText()
        #phones = self.driver.find_elements_by_css_selector("div[class='card-body'] h4") for 18,19 lines
        for phone in phones:
            print(phone.text)
            if phone.text == "Blackberry":
                checkoutPage.addToCart().click()
        self.driver.find_element_by_css_selector("button[class*=btn]").click() #for 24 line
        #confirmPage = checkoutPage.checkOutButton()
        #confirmPage.checkoutbuttonTwo().click()
        checkoutPage.checkOutButton().click() #to reduce no. of methods
        #self.driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click() #for 26th line
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("Ind")
        self.verifyLinkTextPresence("India")
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "suggestions")))  # OR By.LINK_TEXT, "India"
        self.driver.find_element_by_link_text("India").click()
        # driver.find_element_by_id("checkbox2").click()
        # driver.find_element_by_xpath("//input[@id='checkbox2']").click() this line and above line are not working
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        success_text = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
        print(success_text)
        assert "Success!" in success_text

        self.driver.get_screenshot_as_file("screen.png")

