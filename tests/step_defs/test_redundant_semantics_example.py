"""Redundant semantics bad example 3 tests."""
import pytest
from pytest_bdd import given, scenarios, then, when

from pages.bad_examples.bad_example_3 import BadExample3
from pages.main_page import MainPage

scenarios('../features/redundant-semantics-example.feature')


@when('user opens bad example 3 page')
def open_bad_example_3(browser):
    """Open bad example 3 page."""
    MainPage(browser).click_bad_examples_button()
    MainPage(browser).open_bad_example_3()


@then('user checks that heading is displayed')
def is_heading_displayed(browser):
    """Check if heading of bad example 3 is displayed."""
    BadExample3(browser).is_heading_displayed()


@then('user finds button and checks button role presence')
def find_check_redundant_button(browser):
    """User finds and checks button for aria role presence."""
    bad_example_3 = BadExample3(browser)
    button = bad_example_3.find_redundant_button()
    if button.get_attribute('role'):
        button_id = button.get_attribute('id')
        button_role = button.get_attribute('role')
        assert False, f'{button_role} role is found in element with {button_id} id.'


@then('user finds link and checks link role presence')
def find_check_link(browser):
    """Find and check link for link role presence."""
    bad_example_3 = BadExample3(browser)
    link = bad_example_3.find_redundant_link()
    if link.get_attribute('role'):
        link_id = link.get_attribute('id')
        link_role = link.get_attribute('role')
        assert False, f'{link_role} role is found in element with {link_id} id.'


@then('user finds date field and checks combo box role presence')
def find_check_date_field(browser):
    """Find and check date field for combo box role presence."""
    bad_example_3 = BadExample3(browser)
    date_field = bad_example_3.find_redundant_date_field()
    if date_field.get_attribute('role'):
        date_field_id = date_field.get_attribute('id')
        date_field_role = date_field.get_attribute('role')
        assert False, f'{date_field_role} role is found in element with {date_field_id} id.'
