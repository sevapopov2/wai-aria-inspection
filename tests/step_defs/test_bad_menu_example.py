"""Bad menu example step definitions file."""
from pytest_bdd import scenarios, then, when

from pages.bad_examples.bad_example_1 import BadExample1
from pages.main_page import MainPage

scenarios('../features/bad-menu-example.feature')


@when('user opens bad example 1')
def open_bad_example_1(browser):
    """Open bad example 1 page."""
    MainPage(browser).click_bad_examples_button()
    MainPage(browser).open_bad_example_1()


@then('user finds all elements with menuitem role')
def find_all_menuitem_elements(browser):
    """Find all elements with menuitem role on a page."""
    menuitem_list = BadExample1(browser).find_all_menu_item_elements()
    assert menuitem_list
