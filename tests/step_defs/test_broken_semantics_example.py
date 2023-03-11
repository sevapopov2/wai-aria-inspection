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


@then('user finds span button and checks aria role presence')
def find_check_span_button(browser):
    """User finds and checks span button for aria role presence."""
    bad_example_2 = BadExample2(browser)
    broken_button = bad_example_2.find_broken_button()
    if broken_button.get_attribute('role'):
        broken_button_id = broken_button.get_attribute('id')
        broken_button_role = broken_button.get_attribute('role')
        assert False, f'{broken_button_role} role is found in element with {broken_button_id} id.'


@then('user finds span link and checks aria role presence')
def find_check_span_link(browser):
    """Find and check span link for aria role presence."""
    bad_example_2 = BadExample2(browser)
    broken_link = bad_example_2.find_broken_link()
    if broken_link.get_attribute('role'):
        broken_link_id = broken_link.get_attribute('id')
        broken_link_role = broken_link.get_attribute('role')
        assert False, f'{broken_link_role} role is found in element with {broken_link_id} id.'
