# Created by faris at 7/4/2024
Feature: Tests for Target.com cart functionality


  Scenario: User can Navigate to Sign In
    Given Open target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened