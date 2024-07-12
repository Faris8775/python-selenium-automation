# Created by faris at 7/4/2024
Feature: Target cart test


  Scenario: Your shopping cart is empty
    Given Open target main page
    When  Click on Cart icon
    Then  Verify "Your cart is empty" message is shown


  Scenario: Add a mug to cart
    Given Open target main page
    When Search for mug
    Then Verify search results shown for mug
    Then Verify correct search results URL opens for mug
    When Add a mug to cart
    When Add a mug to cart on side bar
    Then Verify item in cart

