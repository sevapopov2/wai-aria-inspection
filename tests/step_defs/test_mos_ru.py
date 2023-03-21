"""Test steps for mos.ru website."""

from pytest_bdd import given, scenarios, then

from pages.mos_ru import MosRu

scenarios('../features/mos-ru.feature')


@given('mos.ru website is opened')
def open_mos_ru_website(browser):
    """Step to open mos.ru website."""
    MosRu(browser).navigate_to_main_page()


@then('main page heading is displayed')
def check_main_page_heading_presence(browser):
    """Check that main page heading is present."""
    MosRu(browser).find_mos_ru_heading()


@then('user checks menuitem role on elements')
def check_menuitem_role_presence(browser):
    """Check menuitem role presence on elements."""
    menuitem_list = MosRu(browser).find_all_menuitem_roles()
    assert menuitem_list
