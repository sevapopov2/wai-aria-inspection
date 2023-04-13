Feature: mos.ru accessibility checks

  Background:
    Given mos.ru website is opened

  Scenario: Check heading presence
    Then main page heading is displayed

  Scenario: Check for menuitem roles on elements
    Then user checks menuitem role on elements

  Scenario: Find span elements with button role
    Then find span elements with button role

  Scenario: Find span elements with link role
    Then find span elements with link role

  Scenario: Find links with link role
    Then find links with link role

  Scenario: Find buttons with button role
    Then find buttons with button role
