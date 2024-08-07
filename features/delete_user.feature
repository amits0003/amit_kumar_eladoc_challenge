Feature: Delete user from the webtable

  Scenario: Delete the user "novak" from the table and validate the user has been deleted
    Given I open the webtable application
    When I delete the user "novak"
    Then I should not see the user "novak" in the table
