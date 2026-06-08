import pytest, re
from playwright.sync_api import expect


class TestAuthenticationPage:
    def test_login_success_with_valid_credentials(self, authentication_page, user_credentials):
        user, password = user_credentials["valid"]

        # GIVEN: The user is on the login page
        # WHEN: The user enters valid credentials
        authentication_page.login(user, password)

        # THEN: The user must see the products dashboard
        expect(authentication_page.page.locator(".title")).to_have_text("Products")

    @pytest.mark.parametrize("user_type, expected_error", [
        ("invalid", "Username and password do not match"),
        ("blank_credentials", "Username is required"),
        ("blank_username", "Username is required"),
        ("blank_password", "Password is required"),
        ("locked", "this user has been locked out"),
    ])
    def test_login_failures(self, authentication_page, user_credentials, user_type, expected_error):
        user, password = user_credentials[user_type]

        # GIVEN: The user is on the login page
        # WHEN: The user enters invalid credentials
        authentication_page.login(user, password)

        # THEN: The user must see the proper error message from the failed login
        expect(authentication_page.get_error_message()).to_contain_text(re.compile(expected_error, re.IGNORECASE))

    def test_attempt_to_go_to_inventory_without_login_in(self, authentication_page):
        # GIVEN: The user is not logged in
        # WHEN: The user attempts to go to inventory page
        authentication_page.navigate_to_product_page()

        # THEN: The user must see the proper error message indicating that you can't go to that page without login in
        expect(authentication_page.get_error_message()).to_contain_text(
            re.compile("You can only access '/inventory.html' when you are logged in.", re.IGNORECASE))

    def test_logout(self, authentication_page, user_credentials):
        user, password = user_credentials["valid"]

        # GIVEN: The user is logged in the product page
        authentication_page.login(user, password)

        # WHEN: The user logs out
        authentication_page.logout()

        # THEN: The user must be in the login page again
        expect(authentication_page.username_input).to_be_visible()
        expect(authentication_page.password_input).to_be_visible()
