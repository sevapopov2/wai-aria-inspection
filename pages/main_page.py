"""Main page class."""

from pages.base_page import BasePage


class MainPage(BasePage):
    """Class of the index page."""

    # Attention! Works only when django development server is running!
    BASE_URL = 'localhost:8000'

    def navigate_to_main_page(self):
        """Navigate to main page method."""
        self.browser.get(self.BASE_URL)
