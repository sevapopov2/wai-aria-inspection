"""Bad example 2 class."""

from pages.base_page import BasePage


class BadExample2(BasePage):
    """Bad example 2 class containing search locators and functions for selenium tests."""

    # Search locators
    BROKEN_SEMANTICS_HEADING = "//h1[@id='broken-semantics-heading']"

    def is_heading_displayed(self):
        """Find and return fixed-semantics-heading."""
        return self.find_element_by_xpath(self.BROKEN_SEMANTICS_HEADING)
