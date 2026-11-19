import random

from playwright.sync_api import Page
from helper.helpers import wait_for_element_to_be_visible

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

    def pick_random_n_products(self, number_of_products_to_add):
        wait_for_element_to_be_visible(self.inventory_items.first)
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
        wait_for_element_to_be_visible(self.inventory_items.first)
        return self.page.locator(self.Locators.CART_ITEMS_COUNTER)

    def get_item_name(self, item):
        return item.locator(self.Locators.ITEM_NAME).inner_text()

    def get_item_description(self, item):
        return item.locator(self.Locators.ITEM_DESCRIPTION).inner_text()

    def get_items_price_list(self):
        all_items_prices_list = self.price_tag.all_inner_texts()
        return [float(price.replace('$', '')) for price in all_items_prices_list]

    def get_product_names_list(self):
        return self.item_name.all_inner_texts()

    def select_filter_option(self, option):
        self.filter.select_option(option)
