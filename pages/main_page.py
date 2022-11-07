"""Main page class."""

from pages.bad_examples.bad_example_1 import BadExample1
from pages.bad_examples.bad_example_2 import BadExample2
from pages.bad_examples.bad_example_3 import BadExample3
from pages.base_page import BasePage
from pages.good_examples.good_example_1 import GoodExample1
from pages.good_examples.good_example_2 import GoodExample2
from pages.good_examples.good_example_3 import GoodExample3


class MainPage(BasePage):
    """Class of the index page."""

    # Attention! Works only when django development server is running!
    BASE_URL = 'http://localhost:8000'

    # Locators
    ABOUT_PROJECT_HEADING = "//h2[@id='about-project']"
    # Bad examples locators
    BAD_EXAMPLES_BUTTON = "//button[@id='bad-examples-button']"
    BAD_EXAMPLE_1_LINK = "//a[@id='bad-example-1']"
    BAD_EXAMPLE_2_LINK = "//a[@id='bad-example-2']"
    BAD_EXAMPLE_3_LINK = "//a[@id='bad-example-3']"
    # Good examples locators
    GOOD_EXAMPLES_BUTTON = "//button[@id='good-examples-button']"
    GOOD_EXAMPLE_1_LINK = "//a[@id='good-example-1']"
    GOOD_EXAMPLE_2_LINK = "//a[@id='good-example-2']"
    GOOD_EXAMPLE_3_LINK = "//a[@id='good-example-3']"

    def navigate_to_main_page(self):
        """Navigate to main page method."""
        self.browser.get(self.BASE_URL)

    def find_about_project_heading(self):
        """Find a heading with the text 'about project'."""
        about_heading = self.find_element_by_xpath(self.ABOUT_PROJECT_HEADING)
        return about_heading

    def click_good_examples_button(self):
        """User clicks good examples button."""
        self.click_element_by_xpath(self.GOOD_EXAMPLES_BUTTON)

    def open_good_example_1(self):
        """Open good example 1 by pressing the link."""
        self.find_element_by_xpath(self.GOOD_EXAMPLE_1_LINK)
        self.click_element_by_xpath(self.GOOD_EXAMPLE_1_LINK)
        return GoodExample1(self.browser)

    def open_good_example_2(self):
        """Open good example 2 by pressing the link."""
        self.find_element_by_xpath(self.GOOD_EXAMPLE_2_LINK)
        self.click_element_by_xpath(self.GOOD_EXAMPLE_2_LINK)
        return GoodExample2(self.browser)

    def open_good_example_3(self):
        """Open good example 3 by pressing the link."""
        self.find_element_by_xpath(self.GOOD_EXAMPLE_3_LINK)
        self.click_element_by_xpath(self.GOOD_EXAMPLE_3_LINK)
        return GoodExample3(self.browser)

    def click_bad_examples_button(self):
        """User clicks bad examples button."""
        self.click_element_by_xpath(self.BAD_EXAMPLES_BUTTON)

    def open_bad_example_1(self):
        """Open bad example 1 by pressing the link."""
        self.find_element_by_xpath(self.BAD_EXAMPLE_1_LINK)
        self.click_element_by_xpath(self.BAD_EXAMPLE_1_LINK)
        return BadExample1(self.browser)

    def open_bad_example_2(self):
        """Open bad example 2 by pressing the link."""
        self.find_element_by_xpath(self.BAD_EXAMPLE_2_LINK)
        self.click_element_by_xpath(self.BAD_EXAMPLE_2_LINK)
        return BadExample2(self.browser)

    def open_bad_example_3(self):
        """Open bad example 3 by pressing the link."""
        self.find_element_by_xpath(self.BAD_EXAMPLE_3_LINK)
        self.click_element_by_xpath(self.BAD_EXAMPLE_3_LINK)
        return BadExample3(self.browser)
