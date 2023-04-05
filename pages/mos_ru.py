"""Test of mos.ru website for aria roles detection."""

from consts.consts import Consts

from pages.base_page import BasePage


class MosRu(BasePage):
    """mos.ru website page object model."""

    MOS_RU_PAGE_TITLE = "//h1[@aria-labelledby='mos-header-title']"


    def navigate_to_main_page(self):
        """Navigate to mos.ru website."""
        self.browser.get(Consts.TEST_URLS['mos_ru_url'])

    def find_mos_ru_heading(self):
        """Find and return mos.ru main page heading."""
        return self.find_element_by_xpath(self.MOS_RU_PAGE_TITLE)

    def find_all_menuitem_roles(self):
        """Find all elements with menuitem roles."""
        return self.find_all_elements_by_xpath(Consts.MENU_ITEM_ROLE)
