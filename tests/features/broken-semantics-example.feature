Feature: bad semantics example testing

  Background:
    Given The index page is loaded

  Scenario: user opens bad example 2 page
    When user opens bad example 2 page
    Then user checks that heading is displayed

  Scenario: User finds all span elements with button role
    When user opens bad example 2 page
    Then user finds all span elements and checks button role presence

  Scenario: User finds all span elements with link role
    When user opens bad example 2 page
    Then user finds all span elements and checks link role presence
