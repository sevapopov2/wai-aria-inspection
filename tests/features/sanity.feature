Feature: Sanity Testing

  Background:
    Given The index page is loaded

  Scenario: user finds about project heading
    Then user finds about project heading

  Scenario: user tests good examples opening
    When user presses good examples button
    Then user presses on good example 1
    And checks that heading is displayed
    Then user presses on good example 2
    And checks that heading is displayed
    Then user presses on good example 3
    And checks that heading is displayed
