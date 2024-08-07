Feature: Add User

  Scenario: Add a new user and validate the user has been added to the table
    Given I open the webtable application
    When I add a new user with the following details
      | First Name | Last Name | User Name | Password | Customer    | Role   | E-mail            | Cell Phone |
      | Amit       | Kumar       | novak   | password | Company AAA | Admin  | amit.kr@gmail.com | 8234525355 |
    Then I should see the user "Amit Kumar" in the table
