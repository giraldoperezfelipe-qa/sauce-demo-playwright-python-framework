from playwright.sync_api import Page


class CartPage:
    class Locators:
        TITLE = ".title"
        ITEM_NAME = ".inventory_item_name"

    def __init__(self, page: Page):
        self.page = page
        self.title = self.page.locator(self.Locators.TITLE)
        self.item_name = page.locator(self.Locators.ITEM_NAME)

    def get_item_name(self):
        return self.item_name.inner_text()
