"""Base Page class."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Base page class that defines all methods to work with page objects."""

    def __init__(self, browser):
        """Class constructor defining webdriver instance and wait function."""
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)

    def find_element_by_xpath(self, xpath):
        """Find element by xpath."""
        return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def find_all_elements_by_xpath(self, xpath):
        """Return all elements found by xpath."""
        items_list = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        if len(items_list) > 0:
            print(len(items_list), 'items are found.')
            print("Listing items' roles and ids.")
            for item in items_list:
                print(item.get_attribute('role'))
                print(item.get_attribute('id'))
            return False
        elif len(items_list) == 0:
            print('No bad items are found. Test passed.')
            return True

    def click_element_by_xpath(self, xpath):
        """Click earlier found by expath method."""
        self.find_element_by_xpath(xpath).click()
