"""Sanity tests to make sure that everything is running."""

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from pages.good_examples.good_example_1 import GoodExample1
from pages.main_page import MainPage

# scenarios path definition
scenarios('../features/sanity.feature')


@then('user finds about project heading')
def find_about_project_heading(browser):
    """Find about project heading."""
    about_heading = MainPage(browser).find_about_project_heading()
    assert about_heading


@when('user presses good examples button')
def good_examples_button_press(browser):
    """User presses good examples button."""
    MainPage(browser).click_good_examples_button()


@then('user presses on good example 1 link')
def open_good_example_1(browser):
    """Open good example 1 page."""
    MainPage(browser).open_good_example_1()


@then('checks that heading is displayed')
def display_good_example_1_heading(browser):
    """Check that good example 1 heading is displayed."""
    example_heading = GoodExample1(browser).is_heading_displayed()
    assert example_heading
