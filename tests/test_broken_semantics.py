"""Broken semantics bad example 2 tests."""

import pytest

from pages.bad_examples.bad_example_2 import BadExample2
from pages.main_page import MainPage


def test_open_bad_example_2(browser):
    """Open bad example 2 and check that heading is displayed."""
    main_page = MainPage(browser)
    bad_example_2 = BadExample2(browser)
    main_page.navigate_to_main_page()
    main_page.click_bad_examples_button()
    main_page.open_bad_example_2()
    bad_example_2.is_heading_displayed()


def test_find_span_button(browser):
    """Find a span with role button."""
    main_page = MainPage(browser)
    bad_example_2 = BadExample2(browser)
    # navigate to index page
    main_page.navigate_to_main_page()
    # Open bad example 2 page
    main_page.click_bad_examples_button()
    main_page.open_bad_example_2()
    # Find span with role button
    broken_button = bad_example_2.find_broken_button()
    if broken_button.get_attribute('role'):
        broken_button_id = broken_button.get_attribute('id')
        broken_button_role = broken_button.get_attribute('role')
        assert False, f'{broken_button_role} role is found in element with {broken_button_id} id.'


def test_find_span_link(browser):
    """Find a span with role link."""
    main_page = MainPage(browser)
    bad_example_2 = BadExample2(browser)
    # navigate to index page
    main_page.navigate_to_main_page()
    # Open bad example 2 page
    main_page.click_bad_examples_button()
    main_page.open_bad_example_2()
    # Find span with role button
    broken_link = bad_example_2.find_broken_link()
    if broken_link.get_attribute('role'):
        broken_link_id = broken_link.get_attribute('id')
        broken_link_role = broken_link.get_attribute('role')
        assert False, f'{broken_link_role} role is found in element with {broken_link_id} id.'
