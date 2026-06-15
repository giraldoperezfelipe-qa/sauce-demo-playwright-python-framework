from playwright.sync_api import expect

from helper.helpers import add_product_to_cart_and_retrieve_its_info


class TestCartPage:
    def test_added_item_has_the_same_name(self, authentication_page, user_credentials, product_page, cart_page):
        # GIVEN: The user is logged in the product page
        user, password = user_credentials["valid"]
        authentication_page.login(user, password)

        # WHEN: The user adds an element from the list to the cart
        item_name_in_product_list, item_description_in_product_list = \
            (add_product_to_cart_and_retrieve_its_info(product_page, "1", True))

        # AND: The user checks the current cart
        product_page.cart_icon.click()

        item_name_in_cart_list = cart_page.get_cart_item_name()
        item_description_in_cart_list = cart_page.get_cart_item_description()

        # THEN: The item in the cart must be the same item selected from the list
        assert item_name_in_product_list == item_name_in_cart_list, \
            f"Item name inside the cart is not the same one for the product in list"

        assert item_description_in_product_list == item_description_in_cart_list, \
            f"Item description inside the cart is not the same one for the product in list"

    def test_remove_item_from_cart(self, authentication_page, user_credentials, product_page, cart_page):
        # GIVEN: The user is logged in the product page
        user, password = user_credentials["valid"]
        authentication_page.login(user, password)

        # AND: The user adds an element from the list to the cart
        add_product_to_cart_and_retrieve_its_info(product_page, "1", False)

        # AND: The user checks the current cart
        product_page.cart_icon.click()

        # WHEN: The user removes the element from the cart list
        cart_page.remove_item_button.click()

        # THEN: The product is no longer in the cart list
        expect(cart_page.item_name).not_to_be_visible()
        expect(cart_page.item_description).not_to_be_visible()
