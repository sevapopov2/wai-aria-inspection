"""Setting up shared fixtures to start and quit Selenium driver."""

from pages.main_page import MainPage

import pytest

from pytest_bdd import given

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    """Inicializing and closing webdriver instance."""
    # Inicialize WebDriver instance
    webbrowser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    # Maximize browser window
    webbrowser.maximize_window()
    # Set up calls to wait for 2 seconds
    webbrowser.implicitly_wait(2)
    # Return webdriver instance
    yield webbrowser
    # Quit the webdriver instance
    webbrowser.quit()


@given('The index page is loaded', target_fixture='load')
def load_index_page(browser):
    """Test that main page loads."""
    main_page = MainPage(browser)
    main_page.navigate_to_main_page()