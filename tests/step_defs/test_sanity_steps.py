"""Sanity tests to make sure that everything is running."""

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from pages.main_page import MainPage

# scenarios path definition
scenarios('../features/sanity.feature')


@then('user finds about project heading')
def find_about_project_heading(browser):
    """Find about project heading."""
    about_heading = MainPage(browser).find_about_project_heading()
    assert about_heading
