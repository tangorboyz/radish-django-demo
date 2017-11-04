## Sample Output

### Sample Output with timezone UTC

```
Feature: User SignUp  # features/signup.feature
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
          | username | email             | password   |
          | john     | john@example.com  | studiocode |
          | john     | johny@example.com | studiocode |
        When first user go to register
        Then the first user should be notified to confirm email address
        And the second user go to register
        But the second user should be notified to pick another username

    Scenario: User register with an email that already used
        Given Two user with the following data
          | username | email            | password   |
          | john     | john@example.com | studiocode |
          | johny    | john@example.com | studiocode |
        When first user go to register
        Then the first user should be notified to confirm email address
        And the second user go to register
        But the second user should be notified that email already exists

1 features (1 passed)
3 scenarios (3 passed)
15 steps (15 passed)
Run 1509777078 finished within 53 seconds
custom timer: -1 day, 16:01:33.283645
```

### Sample Output in UTC+8 (my timezone)

```
Got an error creating the test database: (1007, "Can't create database 'blog_features'; database exists")
Feature: User SignUp  # features/signup.feature
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
          | username | email             | password   |
          | john     | john@example.com  | studiocode |
          | john     | johny@example.com | studiocode |
        When first user go to register
        Then the first user should be notified to confirm email address
        And the second user go to register
        But the second user should be notified to pick another username

    Scenario: User register with an email that already used
        Given Two user with the following data
          | username | email            | password   |
          | john     | john@example.com | studiocode |
          | johny    | john@example.com | studiocode |
        When first user go to register
        Then the first user should be notified to confirm email address
        And the second user go to register
        But the second user should be notified that email already exists

1 features (1 passed)
3 scenarios (3 passed)
15 steps (15 passed)
Run 1509777405 finished within 57 seconds
custom timer: 0:01:31.080446
```