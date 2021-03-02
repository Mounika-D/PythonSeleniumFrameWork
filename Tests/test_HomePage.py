import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


from TestData.HomePageData import TestHomePageData
from pageObjects.HomePage import HomePage
from utilities.baseclass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self , getData):


        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData['FirstName'])
        #driver.find_element_by_css_selector("input[name='name']").send_keys("Mounika")
        homepage.getEmail().send_keys(getData["LastName"])
        #driver.find_element_by_name("email").send_keys("Dommaraju@gmail.com")
        homepage.getPassword().send_keys("abcd@123")
        #driver.find_element_by_css_selector("#exampleInputPassword1").send_keys("abcd@123")  # css selector using only #id
        homepage.clickCheckBox().click()
        #driver.find_element_by_id("exampleCheck1").click()
        self.selectOptionByText(homepage.getGender(), getData["Gender"])
        #dropdown = Select(homepage.getGender()) we moved this to baseclass
        #dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
        #dropdown.select_by_index(0)
        #dropdown.select_by_visible_text("Female") we moved this to baseclass
        homepage.submitForm().click()
        #driver.find_element_by_xpath("//input[@type='submit']").click()
        alertText = homepage.getSuccessMessage().text
        #message = driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text
        print(alertText)
        assert "success" in alertText
        self.driver.refresh()

    @pytest.fixture(params=TestHomePageData.getTestData("Testcase2"))
    def getData(self , request):
        return request.param






import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


from TestData.HomePageData import TestHomePageData
from pageObjects.HomePage import HomePage
from utilities.baseclass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self , getData):


        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["FirstName"])
        homepage.getEmail().send_keys(getData["LastName"])
        homepage.getPassword().send_keys("abcd@123")
        homepage.clickCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["Gender"])
        homepage.submitForm().click()
        alertText = homepage.getSuccessMessage().text
        print(alertText)
        assert "success" in alertText
        self.driver.refresh()

    @pytest.fixture(params=TestHomePageData.getTestData("Testcase2"))
    def getData(self , request):
        return request.param

