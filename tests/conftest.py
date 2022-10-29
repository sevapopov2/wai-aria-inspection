"""Setting up shared fixtures to start and quit Selenium driver."""
import pytest

import selenium.webdriver


@pytest.fixture
def browser():
    """Inicializing and closing webdriver instance."""
    # Inicialize WebDriver instance
    webbrowser = selenium.webdriver.chrome()
    # Maximize browser window
    webbrowser.maximize_window()
    # Set up calls to wait for 2 seconds
    webbrowser.implicitly_wait(2)
    # Return webdriver instance
    yield webbrowser
    # Quit the webdriver instance
    webbrowser.quit()
