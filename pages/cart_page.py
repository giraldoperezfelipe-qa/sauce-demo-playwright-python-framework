from playwright.sync_api import Page


class CartPage:
    class Locators:
        ITEM_NAME = ".inventory_item_name"
        ITEM_DESCRIPTION = ".inventory_item_desc"
        REMOVE_ITEM_BUTTON = ".btn.btn_secondary.btn_small.cart_button"

    def __init__(self, page: Page):
        self.page = page
        self.item_name = page.locator(self.Locators.ITEM_NAME)
        self.item_description = page.locator(self.Locators.ITEM_DESCRIPTION)
        self.remove_item_button = page.locator(self.Locators.REMOVE_ITEM_BUTTON)

    def get_cart_item_name(self):
        return self.item_name.inner_text()

    def get_cart_item_description(self):
        return self.item_description.inner_text()
