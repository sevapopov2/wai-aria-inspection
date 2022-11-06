"""Sanity tests to make sure that everything is running."""

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from pages.good_examples.good_example_1 import GoodExample1
from pages.good_examples.good_example_2 import GoodExample2
from pages.good_examples.good_example_3 import GoodExample3
from pages.main_page import MainPage

# scenarios path definition
scenarios('../features/sanity.feature')


@then('user finds about project heading')
def find_about_project_heading(browser):
    """Find about project heading."""
    about_heading = MainPage(browser).find_about_project_heading()
    assert about_heading


@then('user presses on good example 1 link')
def open_good_example_1(browser):
    """Open good example 1 page."""
    MainPage(browser).open_good_example_1()


@then('good example 1 heading is displayed')
def display_good_example_1_heading(browser):
    """Check that good example 1 heading is displayed."""
    example_heading = GoodExample1(browser).is_heading_displayed()
    assert example_heading


@then('user presses on good example 2 link')
def open_good_example_2(browser):
    """Open good example 2 page."""
    MainPage(browser).open_good_example_2()


@then('good example 2 heading is displayed')
def display_good_example_2_heading(browser):
    """Check that good example 2 heading is displayed."""
    example_heading = GoodExample2(browser).is_heading_displayed()
    assert example_heading


@then('user presses on good example 3 link')
def open_good_example_3(browser):
    """Open good example 3 page."""
    MainPage(browser).open_good_example_3()


@then('good example 3 heading is displayed')
def display_good_example_3_heading(browser):
    """Check that good example 3 heading is displayed."""
    example_heading = GoodExample3(browser).is_heading_displayed()
    assert example_heading
