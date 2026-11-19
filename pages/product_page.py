import random

from playwright.sync_api import Page


class ProductPage:
    class Locators:
        INVENTORY_ITEMS = ".inventory_item"
        ITEM_NAME = ".inventory_item_name"
        CART_ICON = ".shopping_cart_link"
        CART_ITEMS_COUNTER = ".shopping_cart_badge"
        ADD_TO_CART_BUTTON = ".btn.btn_primary.btn_small.btn_inventory"

    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator(self.Locators.INVENTORY_ITEMS)
        self.item_name = page.locator(self.Locators.ITEM_NAME)
        self.cart_icon = page.locator(self.Locators.CART_ICON)
        self.add_to_cart_button = page.locator(self.Locators.ADD_TO_CART_BUTTON)

    def pick_random_n_products(self, number_of_products_to_add):
        self.inventory_items.first.wait_for(state="visible")
        all_items_in_list = self.inventory_items.all()
        number_of_products_in_list = len(all_items_in_list)

        if number_of_products_to_add < 0:
            raise ValueError("Items to add to the cart can only be positive integers, please check")
        elif number_of_products_in_list < number_of_products_to_add:
            raise ValueError("You have requested to add more items to your cart than the currently amount available")
        else:
            # Select random unique items in list, based on the number_of_products
            return random.sample(all_items_in_list, number_of_products_to_add)

    def add_items_to_cart(self, items_to_add):
        for item in items_to_add:
            item.locator(self.add_to_cart_button).click()

    def get_cart_counter(self):
        self.inventory_items.first.wait_for(state="visible")
        return self.page.locator(self.Locators.CART_ITEMS_COUNTER)

    def get_item_name(self, item):
        return item.locator(self.Locators.ITEM_NAME).inner_text()
