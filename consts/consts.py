"""Class with constant variables to share them with other files."""


class Consts:
    """Class with constant variables."""

    # Dictionary with test urls
    TEST_URLS = {
        # Base URL for django wai-aria-inspection website
        'base_url': 'http://localhost:8000',
        'mos_ru_url': 'https://mos.ru'
    }

    # roles variables
    MENU_ITEM_ROLE = "//*[@role='menuitem']"
    BROKEN_SPAN_BUTTON = "//span[@role='button']"
    BROKEN_SPAN_LINK = "//span[@role='link']"
    REDUNDANT_LINK = "//a[@role='link']"
    REDUNDANT_BUTTON = "//button[@role='button']"
    REDUNDANT_DATE_FIELD = "//input[@id='redundant-date']"
