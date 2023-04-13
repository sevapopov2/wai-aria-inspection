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


@then('find span elements with button role')
def find_span_buttons(browser):
    """Find span elements with button role."""
    span_buttons_list = MosRu(browser).find_span_buttons()
    assert span_buttons_list


@then('find span elements with link role')
def find_span_links(browser):
    """Find span elements with link role."""
    span_links_list = MosRu(browser).find_span_links()
    assert span_links_list


@then('find buttons with button role')
def find_redundant_buttons(browser):
    """Find buttons with button role."""
    redundant_buttons_list = MosRu(browser).find_redundant_buttons()
    assert redundant_buttons_list


@then('find links with link role')
def find_redundant_links(browser):
    """Find links with link role."""
    redundant_links_list = MosRu(browser).find_redundant_links()
    assert redundant_links_list
