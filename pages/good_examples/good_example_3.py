"""Good example 3 class."""

from pages.base_page import BasePage


class GoodExample3(BasePage):
    """Good example 3 class containing search locators and methods for Selenium tests."""

    # Search locators
    FIXED_REDUNDANT_SEMANTICS_HEADING = "//h1[@id='fixed-redundant-semantics-heading']"

    def is_heading_displayed(self):
        """Find fixed redundant semantics heading and return it."""
        return self.find_element_by_xpath(self.FIXED_REDUNDANT_SEMANTICS_HEADING)
