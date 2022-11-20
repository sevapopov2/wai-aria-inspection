"""Bad menu example step definitions file."""
import pytest
from pytest_bdd import given, scenarios, then, when

from pages.bad_examples.bad_example_1 import BadExample1
from pages.main_page import MainPage

scenarios('../features/bad-menu-example.feature')


@when('user opens bad example 1')
def open_bad_example_1(browser):
    """Open bad example 1 page."""
    MainPage(browser).click_bad_examples_button()
    MainPage(browser).open_bad_example_1()


@then('user finds link with menuitem role')
def scan_for_menuitem_role(browser):
    """Find link that includes menuitem role."""
    menu_item_link = BadExample1(browser).find_menu_item_element()
    if menu_item_link.get_attribute('role'):
        menu_item_link_id = menu_item_link.get_attribute('id')
        menu_item_link_role = menu_item_link.get_attribute('role')
        assert False, f'{menu_item_link_role} is found in element with{menu_item_link_id} id'
