# Created by faris at 7/4/2024
Feature: Target cart test


  Scenario: Your shopping cart is empty
    Given Open target main page
    When  Click on Cart icon
    Then  Verify "Your cart is empty" message is shown