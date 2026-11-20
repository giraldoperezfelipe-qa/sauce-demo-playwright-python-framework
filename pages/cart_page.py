from playwright.sync_api import Page


class CartPage:
    class Locators:
        TITLE = ".title"
        ITEM_NAME = ".inventory_item_name"
        ITEM_DESCRIPTION = ".inventory_item_desc"
        REMOVE_ITEM_BUTTON = ".btn.btn_secondary.btn_small.cart_button"
        CHECKOUT_BUTTON = "#checkout"
        CART_ITEM = '[data-test="inventory-item"]'

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(self.Locators.TITLE)
        self.item_name = page.locator(self.Locators.ITEM_NAME)
        self.item_description = page.locator(self.Locators.ITEM_DESCRIPTION)
        self.remove_item_button = page.locator(self.Locators.REMOVE_ITEM_BUTTON)
        self.checkout_button = page.locator(self.Locators.CHECKOUT_BUTTON)
        self.cart_item = page.locator(self.Locators.CART_ITEM)

    def get_cart_item_names(self):
        all_cart_items = self.cart_item.all()
        all_inner_texts = []

        for index in range(len(all_cart_items)):
            inner_text = all_cart_items[index].locator(self.item_name).inner_text()
            all_inner_texts.append(inner_text)

        return all_inner_texts

    def remove_items_by_name(self, target_names):
        for item_to_delete_name in target_names:
            matching_item = self.cart_item.filter(has_text=item_to_delete_name)
            matching_item.locator(self.remove_item_button).click()
