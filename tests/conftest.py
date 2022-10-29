"""Setting up shared fixtures to start and quit Selenium driver."""
import pytest

import selenium.webdriver


@pytest.fixture
def browser():
    """Inicializing and closing webdriver instance."""
    # Inicialize WebDriver instance
    webbrowser = selenium.webdriver.chrome()
    # Set up calls to wait for 10 seconds
    webbrowser.implicitly_wait(10)
    # Return webdriver instance
    yield webbrowser
    # Quit the webdriver instance
    webbrowser.quit()
