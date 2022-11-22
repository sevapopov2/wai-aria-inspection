"""bad example 3 class."""

from pages.base_page import BasePage


class BadExample3(BasePage):
    """Bad example 3 class containing search locators and methods for Selenium tests."""

    # Search locators
    REDUNDANT_SEMANTICS_HEADING = "//h1[@id='redundant-semantics-heading']"
    REDUNDANT_LINK = "//a[@id='redundant-link']"
    REDUNDANT_BUTTON = "//button[@id='redundant-button']"
    REDUNDANT_DATE_FIELD = "//input[@id='redundant-date']"

    def is_heading_displayed(self):
        """Find redundant semantics heading and return it."""
        return self.find_element_by_xpath(self.REDUNDANT_SEMANTICS_HEADING)

    def find_redundant_link(self):
        """Find a link and detect if it has a link role."""
        return self.find_element_by_xpath(self.REDUNDANT_LINK)

    def find_redundant_button(self):
        """Find a button and detect if it has aria role."""
        return self.find_element_by_xpath(self.REDUNDANT_BUTTON)

    def find_redundant_date_field(self):
        """Find a date field and detect if it has aria role."""
        return self.find_element_by_xpath(self.REDUNDANT_DATE_FIELD)
