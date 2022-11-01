"""Main page class."""

from pages.base_page import BasePage


class MainPage(BasePage):
    """Class of the index page."""

    # Attention! Works only when django development server is running!
    BASE_URL = 'http://localhost:8000'

    # Locators
    ABOUT_PROJECT_HEADING = "//h2[@id='about-project']"

    def navigate_to_main_page(self):
        """Navigate to main page method."""
        self.browser.get(self.BASE_URL)

    def find_about_project_heading(self):
        """Find a heading with the text 'about project'."""
        about_heading = self.find_element_by_xpath(self.ABOUT_PROJECT_HEADING)
        return about_heading
