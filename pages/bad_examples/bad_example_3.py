"""bad example 3 class."""

from pages.base_page import BasePage


class BadExample3(BasePage):
    """Bad example 3 class containing search locators and methods for Selenium tests."""

    # Search locators
    REDUNDANT_SEMANTICS_HEADING = "//h1[@id='redundant-semantics-heading']"

    def is_heading_displayed(self):
        """Find redundant semantics heading and return it."""
        return self.find_element_by_xpath(self.REDUNDANT_SEMANTICS_HEADING)
