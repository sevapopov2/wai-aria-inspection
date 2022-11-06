"""Good example 2 class."""

from pages.base_page import BasePage


class GoodExample2(BasePage):
    """Good example 2 class containing search locators and functions for selenium tests."""

    # Search locators
    FIXED_BROKEN_SEMANTICS_HEADING = "//h1[@id='fixed-broken-semantics-heading]"

    def find_broken_semantics_heading(self):
        """Find and return fixed-semantics-heading."""
        return self.find_element_by_xpath(self.FIXED_BROKEN_SEMANTICS_HEADING)
