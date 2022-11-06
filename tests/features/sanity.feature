Feature: Sanity Testing

  Background:
    Given The index page is loaded

  Scenario: user finds about project heading
    Then user finds about project heading

  Scenario: user tests good example 1 opening
    When user presses good examples button
    Then user presses on good example 1 link
    Then checks that heading is displayed

  Scenario: user tests good example 1 opening
    When user presses good examples button
    Then user presses on good example 2 link
    Then checks that heading is displayed

  Scenario: user tests good example 3 opening
    When user presses good examples button
    Then user presses on good example 3 link
    Then checks that heading is displayed
