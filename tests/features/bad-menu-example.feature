Feature: bad menu example test

  Background:
    Given The index page is loaded

  Scenario: User finds all elements with menuitem role in bad example 1
    When user opens bad example 1
    Then user finds all elements with menuitem role
