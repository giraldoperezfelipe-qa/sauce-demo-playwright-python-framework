import pytest, re
from playwright.sync_api import expect

from util.constants import AuthenticationErrorMessages


class TestAuthenticationPage:
    def test_login_success_with_valid_credentials(self, authentication_page, user_credentials):
        user, password = user_credentials["valid"]

        # GIVEN: The user is on the login page
        # WHEN: The user enters valid credentials
        authentication_page.login(user, password)

        # THEN: The user must see the products dashboard
        expect(authentication_page.page.locator(".title")).to_have_text("Products")

    @pytest.mark.parametrize("user_type, expected_error", [
        ("invalid", AuthenticationErrorMessages.ERROR_INVALID_CREDENTIALS),
        ("blank_credentials", AuthenticationErrorMessages.ERROR_USERNAME_REQUIRED),
        ("blank_username", AuthenticationErrorMessages.ERROR_USERNAME_REQUIRED),
        ("blank_password", AuthenticationErrorMessages.ERROR_PASSWORD_REQUIRED),
        ("locked", AuthenticationErrorMessages.ERROR_USER_LOCKED),
    ])
    def test_login_failures(self, authentication_page, user_credentials, user_type, expected_error):
        user, password = user_credentials[user_type]

        # GIVEN: The user is on the login page
        # WHEN: The user enters invalid credentials
        authentication_page.login(user, password)

        # THEN: The user must see the proper error message from the failed login
        expect(authentication_page.get_error_message()).to_have_text(re.compile(f"^{expected_error}$", re.IGNORECASE))

    def test_attempt_to_go_to_inventory_without_login_in(self, authentication_page):
        # GIVEN: The user is not logged in
        # WHEN: The user attempts to go to inventory page
        authentication_page.navigate_to_product_page()

        # THEN: The user must see the proper error message indicating that the login failed
        expect(authentication_page.get_error_message()).to_have_text(
            re.compile(f"^{AuthenticationErrorMessages.ERROR_ACCESSING_INVENTORY_NOT_LOGGED_IN}$", re.IGNORECASE))

    def test_logout(self, authentication_page, user_credentials):
        user, password = user_credentials["valid"]

        # GIVEN: The user is logged in the product page
        authentication_page.login(user, password)

        # WHEN: The user logs out
        authentication_page.logout()

        # THEN: The user must be in the login page again
        expect(authentication_page.username_input).to_be_visible()
        expect(authentication_page.password_input).to_be_visible()
