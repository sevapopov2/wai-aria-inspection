from pages.base_page import BasePage

"""Main page class."""
class MainPage(BasePage):
    """Class of the index page."""

    def navigate_to_main_page(self):
        """Navigate to main page method."""
        self.browser.get(self.base_url)
