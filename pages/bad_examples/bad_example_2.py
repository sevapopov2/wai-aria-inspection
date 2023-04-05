"""Bad example 2 class."""

from consts.consts import Consts

from pages.base_page import BasePage


class BadExample2(BasePage):
    """Bad example 2 class containing search locators and functions for selenium tests."""

    # Search locators
    BROKEN_SEMANTICS_HEADING = "//h1[@id='broken-semantics-aria-heading']"


    def is_heading_displayed(self):
        """Find and return broken-semantics-heading."""
        return self.find_element_by_xpath(self.BROKEN_SEMANTICS_HEADING)

    def find_broken_buttons(self):
        """Find all span tags with button role."""
        return self.find_all_elements_by_xpath(Consts.BROKEN_SPAN_BUTTON)

    def find_broken_links(self):
        """Find all span tags with link role."""
        return self.find_all_elements_by_xpath(Consts.BROKEN_SPAN_LINK)
