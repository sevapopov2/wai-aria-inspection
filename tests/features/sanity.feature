Feature: Sanity Testing

  Background:
    Given The index page is loaded

  Scenario: user finds about project heading
    Then user finds about project heading

  Scenario: user tests good example 1 opening
    When user presses good examples button
    Then user presses on good example 1 link
    Then good example 1 heading is displayed

  Scenario: user tests good example 2 opening
    When user presses good examples button
    Then user presses on good example 2 link
    Then good example 2 heading is displayed

  Scenario: user tests good example 3 opening
    When user presses good examples button
    Then user presses on good example 3 link
    Then good example 3 heading is displayed

Scenario: user tests bad example 1 opening
    When user presses bad examples button
    Then user presses on bad example 1 link
    Then bad example 1 heading is displayed

  Scenario: user tests bad example 2 opening
    When user presses bad examples button
    Then user presses on bad example 2 link
    Then bad example 2 heading is displayed

  Scenario: user tests bad example 3 opening
    When user presses bad examples button
    Then user presses on bad example 3 link
    Then bad example 3 heading is displayed
