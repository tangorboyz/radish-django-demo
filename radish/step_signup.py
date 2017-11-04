import time

from hamcrest import assert_that, contains_string
from radish import steps
from radish.scenario import Step
from selenium.webdriver import Chrome
from selenium.common.exceptions import WebDriverException

from util import wait_for_element


@steps
class EmailConfirmationAfterSignUp:
    """A user get confirmation email after registration"""

    def prepare_data(self, step: Step):
        """I have the following data"""
        step.context.user_data = {
            'username': step.table[0]['username'],
            'email': step.table[0]['email'],
            'password': step.table[0]['password']
        }

    def go_to_home_page(self, step: Step):
        """I go to the home page"""
        step.context.browser.get(step.context.base_url)

    def click_signup_link(self, step: Step):
        """I see an option to register and click"""
        find_by_link = Chrome.find_element_by_link_text.__name__
        link = wait_for_element(
            step.context.browser, find_by_link, "Sign Up")
        link.click()

    def submit_data(self, step: Step):
        """I submit my data on the registration form"""
        user_data = step.context.user_data
        browser = step.context.browser
        find_by_id = Chrome.find_element_by_id.__name__
        username_input = wait_for_element(browser, find_by_id, 'id_username')
        email_input = wait_for_element(browser, find_by_id, 'id_email')
        password1_input = wait_for_element(browser, find_by_id, 'id_password1')
        password2_input = wait_for_element(
            browser, find_by_id, 'id_password2')
        submit = wait_for_element(browser, find_by_id, 'signup')

        username_input.send_keys(user_data['username'])
        email_input.send_keys(user_data['email'])
        password1_input.send_keys(user_data['password'])
        password2_input.send_keys(user_data['password'])
        submit.click()

    def email_confirmation_sent(self, step: Step):
        """I should be notified to confirm my email address"""
        browser = step.context.browser
        find_by_tag = Chrome.find_element_by_tag_name.__name__
        h1 = wait_for_element(browser, find_by_tag, 'h1')
        assert_that(h1.text, contains_string('Verify Your E-mail Address'))


@steps
class RegisterWithAlreadyUsedUsername:
    """User cannot register with username that already used"""

    def prepare_user_data(self, step: Step):
        """Two user with the following data"""
        self.data1 = {key: step.table[0][key] for key in step.table[0]}
        self.data2 = {key: step.table[1][key] for key in step.table[1]}

    def first_user_register(self, step: Step):
        """first user go to register"""
        base_url = step.context.base_url
        browser = step.context.browser
        browser.get(base_url)
        find_by_link = Chrome.find_element_by_link_text.__name__
        find_by_id = Chrome.find_element_by_id.__name__

        login_link = wait_for_element(
            browser, find_by_link, 'Sign Up')
        login_link.click()

        username_input = wait_for_element(browser, find_by_id, 'id_username')
        email_input = wait_for_element(browser, find_by_id, 'id_email')
        password1_input = wait_for_element(browser, find_by_id, 'id_password1')
        password2_input = wait_for_element(
            browser, find_by_id, 'id_password2')
        submit = wait_for_element(browser, find_by_id, 'signup')

        username_input.send_keys(self.data1['username'])
        email_input.send_keys(self.data1['email'])
        password1_input.send_keys(self.data1['password'])
        password2_input.send_keys(self.data1['password'])
        submit.click()

    def confirmation_email_is_sent_for_first_user(self, step: Step):
        """the first user should be notified to confirm email address"""
        browser = step.context.browser
        find_by_tag = Chrome.find_element_by_tag_name.__name__
        h1 = wait_for_element(browser, find_by_tag, 'h1')
        assert_that(h1.text, contains_string("Verify Your E-mail Address"))
        browser.quit()

    def second_user_register(self, step: Step):
        """the second user go to register"""
        base_url = step.context.base_url
        step.context.browser = Chrome()
        browser = step.context.browser
        browser.get(base_url)
        find_by_link = Chrome.find_element_by_link_text.__name__
        find_by_id = Chrome.find_element_by_id.__name__

        login_link = wait_for_element(
            browser, find_by_link, 'Sign Up')
        login_link.click()

        username_input = wait_for_element(browser, find_by_id, 'id_username')
        email_input = wait_for_element(browser, find_by_id, 'id_email')
        password1_input = wait_for_element(browser, find_by_id, 'id_password1')
        password2_input = wait_for_element(
            browser, find_by_id, 'id_password1')
        submit = wait_for_element(browser, find_by_id, 'signup')

        username_input.send_keys(self.data2['username'])
        email_input.send_keys(self.data2['email'])
        password1_input.send_keys(self.data2['password'])
        password2_input.send_keys(self.data2['password'])
        submit.click()

    def second_user_been_notified_about_duplicate_username(self, step):
        """the second user should be notified to pick another username"""
        find_by_tag = Chrome.find_element_by_tag_name.__name__
        body = wait_for_element(step.context.browser, find_by_tag, 'body')
        assert_that(body.text, contains_string(
            "A user with that username already exists"))


@steps
class SignupWithAlreadyUsedEmail:
    """User register with an email that already used"""
    def second_user_been_notfied_about_duplicate_email(self, step):
        """the second user should be notified that email already exists"""
        find_by_tag = Chrome.find_element_by_tag_name.__name__
        body = wait_for_element(step.context.browser, find_by_tag, 'body')
        assert_that(body.text, contains_string(
            "A user is already registered with this e-mail address."))
