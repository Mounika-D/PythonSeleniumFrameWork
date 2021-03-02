import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkTextPresence(self , text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))  # OR By.LINK_TEXT, "India

    def selectOptionByText(self ,locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)