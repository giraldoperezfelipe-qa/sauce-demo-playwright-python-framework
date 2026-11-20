from helper.helpers import *


class TestCartPage:
    def test_added_items_have_the_same_name_in_cart(self, authentication_page, user_credentials, product_page,
                                                    cart_page):
        products_to_add = 2

        # GIVEN: The user is logged in the product page
        user, password = user_credentials["valid"]
        authentication_page.login(user, password)

        # WHEN: The user adds some elements from the list to the cart
        product_list = add_n_products_to_cart_and_retrieve_them(product_page, products_to_add)
        item_names_added_to_cart = retrieve_names_from_products(product_list, cart_page.item_name)

        # AND: The user checks the current cart
        product_page.cart_icon.click()

        expect(cart_page.page).to_have_url("https://www.saucedemo.com/cart.html")
        expect(cart_page.cart_item).to_have_count(products_to_add)
        item_names_in_cart = cart_page.get_cart_item_names()

        # THEN: The items in the cart must be the same items selected from the list
        assert sorted(item_names_added_to_cart) == sorted(item_names_in_cart), \
            f"Items inside the cart aren't the same ones added from product list, please check"

    def test_remove_items_from_cart(self, authentication_page, user_credentials, product_page, cart_page):
        products_to_add = 2

        # GIVEN: The user is logged in the product page
        user, password = user_credentials["valid"]
        authentication_page.login(user, password)

        # AND: The user adds some elements from the list to the cart
        add_n_products_to_cart_and_retrieve_them(product_page, 2)

        # AND: The user checks the current cart
        product_page.cart_icon.click()

        expect(cart_page.page).to_have_url("https://www.saucedemo.com/cart.html")
        expect(cart_page.cart_item).to_have_count(products_to_add)
        item_names_in_cart = cart_page.get_cart_item_names()

        # WHEN: The user removes the element from the cart list
        cart_page.remove_items_by_name(item_names_in_cart)

        # THEN: The cart list is empty
        expect(cart_page.item_name).not_to_be_visible()
        expect(cart_page.item_description).not_to_be_visible()
