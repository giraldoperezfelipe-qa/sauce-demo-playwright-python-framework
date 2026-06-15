import random
from playwright.sync_api import Page


class ProductPage:
    class Locators:
        INVENTORY_ITEMS = ".inventory_item"
        ITEM_NAME = ".inventory_item_name"
        ITEM_DESCRIPTION = ".inventory_item_desc"
        CART_ICON = ".shopping_cart_link"
        CART_ITEMS_COUNTER = ".shopping_cart_badge"
        ADD_TO_CART_BUTTON = ".btn.btn_primary.btn_small.btn_inventory"
        FILTER = ".product_sort_container"
        PRICE_TAG = ".inventory_item_price"

    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator(self.Locators.INVENTORY_ITEMS)
        self.item_name = page.locator(self.Locators.ITEM_NAME)
        self.item_description = page.locator(self.Locators.ITEM_DESCRIPTION)
        self.cart_icon = page.locator(self.Locators.CART_ICON)
        self.add_to_cart_button = page.locator(self.Locators.ADD_TO_CART_BUTTON)
        self.filter = page.locator(self.Locators.FILTER)
        self.price_tag = page.locator(self.Locators.PRICE_TAG)

    def pick_random_item(self):
        items = self.inventory_items.all()
        if not items:
            raise RuntimeError("No inventory items found on the page.")

        return random.choice(items)

    def add_to_cart_an_item(self, item):
        item.locator(self.add_to_cart_button).click()

    def get_cart_counter(self):
        return self.page.locator(self.Locators.CART_ITEMS_COUNTER)

    def get_item_name(self, item):
        return item.locator(self.Locators.ITEM_NAME).inner_text()

    def get_item_description(self, item):
        return item.locator(self.Locators.ITEM_DESCRIPTION).inner_text()

    def get_items_price_list(self):
        all_items_prices_list = self.price_tag.all_inner_texts()
        return [float(price.replace('$', '')) for price in all_items_prices_list]

    def select_low_to_high_option(self):
        self.filter.select_option("lohi")
