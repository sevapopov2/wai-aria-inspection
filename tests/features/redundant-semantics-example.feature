Feature: redundant semantics example testing

  Background:
    Given The index page is loaded

  Scenario: user opens bad example 3 page
    When user opens bad example 3 page
    Then user checks that heading is displayed

  Scenario: User finds button with aria role
    When user opens bad example 3 page
    Then user finds button and checks button role presence

  Scenario: User finds link with aria role
    When user opens bad example 3 page
    Then user finds link and checks link role presence

  Scenario: User finds date field with aria role
    When user opens bad example 3 page
    Then user finds date field and checks combo box role presence
