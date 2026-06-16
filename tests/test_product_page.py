from playwright.sync_api import expect
from util.constants import ProductFilterOptions
from helper.helpers import add_product_to_cart_and_retrieve_its_info


class TestProductPage:
    def test_adding_one_element_to_the_cart(self, authentication_page, user_credentials, product_page):
        user, password = user_credentials["valid"]

        # GIVEN: The user is logged in the product page
        authentication_page.login(user, password)

        # WHEN: The user adds an element from the list to the cart
        # THEN: The shopping cart has 1 new product
        add_product_to_cart_and_retrieve_its_info(product_page, "1", False)

    def test_item_still_in_the_cart_after_logout(self, authentication_page, user_credentials, product_page):
        # GIVEN: The user is logged in the product page
        # AND: The user has added an item to the shopping cart
        self.test_adding_one_element_to_the_cart(authentication_page, user_credentials, product_page)

        # AND: The user logs out
        authentication_page.logout()

        # WHEN: THe user logs again in his account
        user, password = user_credentials["valid"]
        authentication_page.login(user, password)

        # THEN: The shopping cart still has 1 product added
        expect(product_page.get_cart_counter()).to_have_text("1")

    def test_item_must_not_be_in_other_user_cart(self, authentication_page, user_credentials, product_page):
        # GIVEN: The user is logged in the product page
        # AND: The user has added an item to the shopping cart
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

    def test_a_to_z_product_filter(self, authentication_page, user_credentials, product_page):
        user, password = user_credentials["valid"]

        # GIVEN: The user is logged in the product page
        authentication_page.login(user, password)

        # WHEN: The user sorts the products by name from A to Z
        product_page.select_filter_option(ProductFilterOptions.NAME_A_TO_Z)

        # THEN: The items must be sorted by name from A to Z
        product_names_list = product_page.get_product_names_list()
        assert product_names_list == sorted(product_names_list), f"List is not sorted A to Z: {product_names_list}"

    def test_z_to_a_product_filter(self, authentication_page, user_credentials, product_page):
        user, password = user_credentials["valid"]

        # GIVEN: The user is logged in the product page
        authentication_page.login(user, password)

        # WHEN: The user sorts the products by name from Z to A
        product_page.select_filter_option(ProductFilterOptions.NAME_Z_TO_A)

        # THEN: The items must be sorted by name from Z to A
        product_names_list = product_page.get_product_names_list()
        assert product_names_list == sorted(product_names_list,
                                            reverse=True), f"List is not sorted Z to A: {product_names_list}"

    def test_low_to_high_price_product_filter(self, authentication_page, user_credentials, product_page):
        user, password = user_credentials["valid"]

        # GIVEN: The user is logged in the product page
        authentication_page.login(user, password)

        # WHEN: The user sorts the products by price from low to high
        product_page.select_filter_option(ProductFilterOptions.PRICE_LOW_TO_HIGH)

        # THEN: The items must be sorted from low to high by price
        items_prices_list_clean = product_page.get_items_price_list()

        for price in range(len(items_prices_list_clean) - 1):
            current_price = items_prices_list_clean[price]
            next_price = items_prices_list_clean[price + 1]

            # Assert that current price is less than, or equal, to the next price in the list
            assert current_price <= next_price, f"Sort filter failed! {current_price} is greater than {next_price}"

    def test_high_to_low_price_product_filter(self, authentication_page, user_credentials, product_page):
        user, password = user_credentials["valid"]

        # GIVEN: The user is logged in the product page
        authentication_page.login(user, password)

        # WHEN: The user sorts the products by price from high to low
        product_page.select_filter_option(ProductFilterOptions.PRICE_HIGH_TO_LOW)

        # THEN: The items must be sorted from low to high by price
        items_prices_list_clean = product_page.get_items_price_list()

        for price in range(len(items_prices_list_clean) - 1):
            current_price = items_prices_list_clean[price]
            next_price = items_prices_list_clean[price + 1]

            # Assert that current price is less than, or equal, to the next price in the list
            assert current_price >= next_price, f"Sort filter failed! {current_price} is greater than {next_price}"
