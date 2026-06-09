from playwright.sync_api import expect

from helper.helpers import add_product_to_cart_and_retrieve_its_name


class TestProductPage:
    def test_adding_one_element_to_the_cart(self, authentication_page, user_credentials, product_page):
        user, password = user_credentials["valid"]

        # GIVEN: The user is logged in the product page
        authentication_page.login(user, password)

        # WHEN: The user adds an element from the list to the cart
        # THEN: The shopping cart has 1 new product
        add_product_to_cart_and_retrieve_its_name(product_page, "1")

    def test_item_still_in_the_cart_after_logout(self, authentication_page, user_credentials, product_page):
        # GIVEN: The user has added an item to the shopping cart
        self.test_adding_one_element_to_the_cart(authentication_page, user_credentials, product_page)

        # AND: The user logs out
        authentication_page.logout()

        # WHEN: THe user logs again in his account
        user, password = user_credentials["valid"]
        authentication_page.login(user, password)

        # THEN: The shopping cart still has 1 product added
        expect(product_page.get_cart_counter()).to_have_text("1")

    def test_item_must_not_be_in_other_user_cart(self, authentication_page, user_credentials, product_page):
        # GIVEN: The user has added an item to the shopping cart
        self.test_adding_one_element_to_the_cart(authentication_page, user_credentials, product_page)

        # AND: The user logs out
        authentication_page.logout()

        # WHEN: Another user logs in
        authentication_page.login("problem_user", "secret_sauce")

        # THEN: The shopping cart must be empty
        expect(
            product_page.get_cart_counter(),
            "The cart should be empty, this account never added any product to the cart"
        ).not_to_be_visible()
