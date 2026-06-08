from playwright.sync_api import expect


class TestProductPage:
    def test_adding_one_element_to_the_cart(self, authentication_page, user_credentials, product_page):
        user, password = user_credentials["valid"]

        # GIVEN: The user is logged in the product page
        authentication_page.login(user, password)

        # WHEN: The user selects any product in the list
        product_page.add_to_cart_a_random_product_from_the_list()

        # THEN: The shopping cart has 1 new product
        expect(product_page.get_cart_counter()).to_have_text("1")

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

        # THEN: The shopping cart items counter must not be visible
        expect(product_page.get_cart_counter()).not_to_be_visible()
