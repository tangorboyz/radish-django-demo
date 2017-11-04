Feature: User SignUp
    In order to comment or subscribe particular blog post
    then user need to have an account

   Scenario: A user get confirmation email after registration
        Given I have the following data
            | username | email            | password   |
            | john     | john@example.com | studiocode |
        When I go to the home page
        And I see an option to register and click
        And I submit my data on the registration form
        Then I should be notified to confirm my email address

    Scenario: User cannot register with username that already used
        Given Two user with the following data
            | username | email             | password |
            | john     | john@example.com  | studiocode |
            | john     | johny@example.com | studiocode |
        When first user go to register
        Then the first user should be notified to confirm email address
        And the second user go to register
        But the second user should be notified to pick another username 

    Scenario: User register with an email that already used
        Given Two user with the following data
            | username  | email             | password   |
            | john      | john@example.com  | studiocode |
            | johny     | john@example.com  | studiocode |
        When first user go to register 
        Then the first user should be notified to confirm email address
        And the second user go to register
        But the second user should be notified that email already exists
