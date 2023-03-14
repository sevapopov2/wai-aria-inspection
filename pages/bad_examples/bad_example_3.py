"""bad example 3 class."""

from pages.base_page import BasePage


class BadExample3(BasePage):
    """Bad example 3 class containing search locators and methods for Selenium tests."""

    # Search locators
    REDUNDANT_SEMANTICS_HEADING = "//h1[@id='redundant-semantics-heading']"
    REDUNDANT_LINK = "//a[@role='link']"
    REDUNDANT_BUTTON = "//button[@role='button']"
    REDUNDANT_DATE_FIELD = "//input[@id='redundant-date']"

    def is_heading_displayed(self):
        """Find redundant semantics heading and return it."""
        return self.find_element_by_xpath(self.REDUNDANT_SEMANTICS_HEADING)

    def find_redundant_links(self):
        """Find all links and detect if they have a link role."""
        return self.find_all_elements_by_xpath(self.REDUNDANT_LINK)

    def find_redundant_buttons(self):
        """Find all buttons and detect if they have button role."""
        return self.find_all_elements_by_xpath(self.REDUNDANT_BUTTON)

    def find_redundant_date_field(self):
        """Find a date field and detect if it has aria role."""
        return self.find_element_by_xpath(self.REDUNDANT_DATE_FIELD)
