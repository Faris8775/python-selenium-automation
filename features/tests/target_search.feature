# Created by faruk at 6/30/2024
Feature: Target main page search tests

  Scenario: User can search for a product on target
    Given Open target main page
    When Search for product
    Then Verify search worked

  # Make sure scenario names are unique:
  Scenario: User can search for a product2 on target
    Given Open target main page