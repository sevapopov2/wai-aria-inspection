Feature: mos.ru accessibility checks

  Background:
    Given mos.ru website is opened

  Scenario: Check heading presence
    Then main page heading is displayed

  Scenario: Check for menuitem roles on elements
    Then user checks menuitem role on elements
