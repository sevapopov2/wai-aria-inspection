"""Broken semantics bad example 2 tests."""
from pytest_bdd import scenarios, then, when

from pages.bad_examples.bad_example_2 import BadExample2
from pages.main_page import MainPage

scenarios('../features/broken-semantics-example.feature')


@when('user opens bad example 2 page')
def open_bad_example_2(browser):
    """Open bad example 2 page."""
    MainPage(browser).click_bad_examples_button()
    MainPage(browser).open_bad_example_2()


@then('user checks that heading is displayed')
def is_heading_displayed(browser):
    """Check if heading of bad example 2 is displayed."""
    BadExample2(browser).is_heading_displayed()


@then('user finds all span elements and checks button role presence')
def find_check_span_buttons(browser):
    """User finds and checks all span elements for button role presence."""
    broken_buttons_list = BadExample2(browser).find_broken_buttons()
    assert broken_buttons_list


@then('user finds all span elements and checks link role presence')
def find_check_span_links(browser):
    """Find and check all span links for aria role presence."""
    broken_links_list = BadExample2(browser).find_broken_links()
    assert broken_links_list
