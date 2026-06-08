import random
from playwright.sync_api import Page


class ProductPage:
    class Locators:
        INVENTORY_ITEMS = ".inventory_item"
        CART_ITEMS_COUNTER = ".shopping_cart_badge"
        CART_ICON = ".shopping_cart_link"
        ADD_TO_CART_BUTTON = ".btn.btn_primary.btn_small.btn_inventory"

    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator(self.Locators.INVENTORY_ITEMS)
        self.add_to_cart_button = page.locator(self.Locators.ADD_TO_CART_BUTTON)
        self.cart_icon = page.locator(self.Locators.CART_ICON)

    def add_to_cart_a_random_product_from_the_list(self):
        items = self.inventory_items.all()
        if not items:
            raise RuntimeError("No inventory items found on the page.")

        random_item = random.choice(items)
        random_item.locator(self.add_to_cart_button).click()

    def get_cart_counter(self):
        return self.page.locator(self.Locators.CART_ITEMS_COUNTER)
