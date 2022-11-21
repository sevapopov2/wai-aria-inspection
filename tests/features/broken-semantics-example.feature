Feature: bad semantics example testing

  Background:
    Given The index page is loaded

  Scenario: user opens bad example 2 page
    When user opens bad example 2 page
    Then user checks that heading is displayed

  Scenario: User finds span button with aria role
    When user opens bad example 2 page
    Then user finds span button and checks aria role presence

  Scenario: User finds span link with aria role
    When user opens bad example 2 page
    Then user finds span link and checks aria role presence
