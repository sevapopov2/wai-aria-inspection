Feature: redundant semantics example testing

  Background:
    Given The index page is loaded

  Scenario: user opens bad example 3 page
    When user opens bad example 3 page
    Then user checks that heading is displayed

  Scenario: User finds all buttons with aria role
    When user opens bad example 3 page
    Then user finds all buttons and checks button role presence

  Scenario: User finds all links with aria role
    When user opens bad example 3 page
    Then user finds all links and checks link role presence

  Scenario: User finds date field with aria role
    When user opens bad example 3 page
    Then user finds date field and checks combo box role presence
