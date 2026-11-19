from helper.helpers import *


class TestCartPage:

    def test_added_items_have_the_same_name_in_cart(self, authentication_page, user_credentials, product_page, cart_page):
        # GIVEN: The user is logged in the product page
        user, password = user_credentials["valid"]
        authentication_page.login(user, password)

        # WHEN: The user adds an element from the list to the cart
        product_list = add_n_products_to_cart_and_retrieve_them(product_page, 2)
        item_names_added_to_cart = retrieve_names_from_products(product_list, cart_page.item_name)

        # AND: The user checks the current cart
        product_page.cart_icon.click()

        wait_for_element_to_be_visible(cart_page.title)
        item_names_in_cart = cart_page.get_cart_item_names()

        # THEN: The item in the cart must be the same item selected from the list
        assert item_names_added_to_cart == item_names_in_cart, \
            f"Items inside the cart aren't the same ones added from product list, please check"

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
