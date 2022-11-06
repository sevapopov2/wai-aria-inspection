"""Good example 1 class."""

from pages.base_page import BasePage


class GoodExample1(BasePage):
    """Page object model for good menu example.

    Search locators and methods are included here for Selenium tests.
    """

    # Search locators
    GOOD_MENU_EXAMPLE_HEADING = "//h1[@id='good-menu-example-heading']"

    def is_heading_displayed(self):
        """Find and return heading to check if it is displayed in test."""
        return self.find_element_by_xpath(self.GOOD_MENU_EXAMPLE_HEADING)
