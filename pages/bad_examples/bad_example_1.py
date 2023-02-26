"""Bad example 1 class."""

from pages.base_page import BasePage


class BadExample1(BasePage):
    """Page object model for bad menu example.

    Search locators and methods are included here for Selenium tests.
    """

    # Search locators
    BAD_MENU_EXAMPLE_HEADING = "//h1[@id='bad-menu-example-heading']"
    MENU_ITEM_ELEMENT = "//*[@role='menuitem']"

    def is_heading_displayed(self):
        """Find and return heading to check if it is displayed in test."""
        return self.find_element_by_xpath(self.BAD_MENU_EXAMPLE_HEADING)

    def find_menu_item_element(self):
        """Find and return link with menuitem role."""
        return self.find_element_by_xpath(self.MENU_ITEM_ELEMENT)

    def find_all_menu_item_elements(self):
        """Find and return the list of all elements with menuitem role on a page."""
        return self.find_all_elements_by_xpath(self.MENU_ITEM_ELEMENT)
