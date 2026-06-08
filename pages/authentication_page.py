from playwright.sync_api import Page


class AuthenticationPage:
    class Locators:
        USERNAME_PLACEHOLDER = "#user-name"
        PASSWORD_PLACEHOLDER = "#password"
        LOGIN_BUTTON = "#login-button"
        MENU_BUTTON = "#react-burger-menu-btn"
        LOGOUT_BUTTON = "#logout_sidebar_link"
        ERROR_MESSAGE = '[data-test="error"]'

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator(self.Locators.USERNAME_PLACEHOLDER)
        self.password_input = page.locator(self.Locators.PASSWORD_PLACEHOLDER)
        self.login_button = page.locator(self.Locators.LOGIN_BUTTON)
        self.menu_button = page.locator(self.Locators.MENU_BUTTON)
        self.logout_button = page.locator(self.Locators.LOGOUT_BUTTON)

    def navigate_to_login_page(self):
        self.page.goto("https://www.saucedemo.com/")

    def navigate_to_product_page(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def get_error_message(self):
        return self.page.locator(self.Locators.ERROR_MESSAGE)

    def login(self, username, password):
        self.navigate_to_login_page()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def logout(self):
        self.menu_button.click()
        self.logout_button.click()