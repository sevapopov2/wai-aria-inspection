Feature: Sanity Testing

  Background: 
    Given The index page is loaded

  Scenario: user finds "О проекте" heading
    Then user finds a heading "О проекте"
