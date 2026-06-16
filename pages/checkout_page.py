from playwright.sync_api import Page

from util.constants import CheckoutFormInfo


class CheckoutPage:
    class Locators:
        FIRST_NAME_INPUT = "#first-name"
        LAST_NAME_INPUT = "#last-name"
        POSTAL_CODE = "#postal-code"
        CONTINUE_BUTTON = "#continue"
        PRODUCT_NAME = ".inventory_item_name"
        PRODUCT_DESCRIPTION = ".inventory_item_desc"
        FINISH_BUTTON = "#finish"
        CHECKOUT_CHECK_ICON = ".pony_express"
        CONFIRMATION_TITLE = ".complete-header"
        CONFIRMATION_TEXT = ".complete-text"

    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator(self.Locators.FIRST_NAME_INPUT)
        self.last_name_input = page.locator(self.Locators.LAST_NAME_INPUT)
        self.postal_code_input = page.locator(self.Locators.POSTAL_CODE)
        self.continue_button = page.locator(self.Locators.CONTINUE_BUTTON)
        self.product_name = page.locator(self.Locators.PRODUCT_NAME)
        self.product_description = page.locator(self.Locators.PRODUCT_DESCRIPTION)
        self.finish_button = page.locator(self.Locators.FINISH_BUTTON)
        self.checkout_check_icon = page.locator(self.Locators.CHECKOUT_CHECK_ICON)
        self.confirmation_title = page.locator(self.Locators.CONFIRMATION_TITLE)
        self.confirmation_text = page.locator(self.Locators.CONFIRMATION_TEXT)

    def fill_checkout_form(self):
        self.first_name_input.fill(CheckoutFormInfo.FIRST_NAME)
        self.last_name_input.fill(CheckoutFormInfo.LAST_NAME)
        self.postal_code_input.fill(CheckoutFormInfo.ZIP_CODE)
