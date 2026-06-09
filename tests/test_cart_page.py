from helper.helpers import add_product_to_cart_and_retrieve_its_name


class TestCartPage:
    def test_added_item_has_the_same_name(self, authentication_page, user_credentials, product_page, cart_page):
        # GIVEN: The user is logged in the product page
        user, password = user_credentials["valid"]
        authentication_page.login(user, password)

        # WHEN: The user adds an element from the list to the cart
        item_name_in_product_list = add_product_to_cart_and_retrieve_its_name(product_page, "1")

        # AND: The user checks the current cart
        product_page.cart_icon.click()

        item_name_in_cart_list = cart_page.get_item_name()

        # THEN: The item in the cart must be the same item selected from the list
        assert item_name_in_product_list == item_name_in_cart_list, \
            f"Item inside the cart is not the same one selected in products list"
