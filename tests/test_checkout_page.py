import re

import pytest
from playwright.sync_api import expect

from conftest import checkout_page
from helper.helpers import add_product_to_cart_and_retrieve_its_info

from util.constants import CheckoutMessages
from util.constants import CheckoutFormErrorMessages
from util.constants import CheckoutFormInfo


class TestCheckoutPage:
    def test_send_checkout_form(self, authentication_page, user_credentials, product_page, cart_page, checkout_page):
        # GIVEN: The user is logged in the product page
        user, password = user_credentials["valid"]
        authentication_page.login(user, password)

        # AND: The user adds an element from the list to the cart
        item_name_in_product_list, item_description_in_product_list = \
            (add_product_to_cart_and_retrieve_its_info(product_page, "1", True))
        product_page.cart_icon.click()

        # WHEN: The user sends the checkout form
        cart_page.checkout_button.click()
        checkout_page.fill_checkout_form(CheckoutFormInfo.FIRST_NAME, CheckoutFormInfo.LAST_NAME,
                                         CheckoutFormInfo.ZIP_CODE)
        checkout_page.continue_button.click()

        item_name_in_checkout = checkout_page.product_name.inner_text()
        item_description_in_checkout = checkout_page.product_description.inner_text()

        assert item_name_in_product_list == item_name_in_checkout, \
            f"Item name inside the checkout is not the same one for the product in list"

        assert item_description_in_product_list == item_description_in_checkout, \
            f"Item description inside the checkout is not the same one for the product in list"

        checkout_page.finish_button.click()

        # THEN: A confirmation view is displayed for the user
        expect(checkout_page.checkout_check_icon).to_be_visible()
        expect(checkout_page.confirmation_text).to_be_visible()
        expect(checkout_page.confirmation_title).to_be_visible()

        assert checkout_page.confirmation_title.inner_text() == CheckoutMessages.CHECKOUT_TITLE, \
            f"Confirmation title is not correct, please check"

        assert checkout_page.confirmation_text.inner_text() == CheckoutMessages.CHECKOUT_TEXT, \
            f"Confirmation title is not correct, please check"

    @pytest.mark.parametrize("checkout_form_fill_out_type, expected_error", [
        ("every_entry_blank", CheckoutFormErrorMessages.ERROR_FIRST_NAME_REQUIRED),
        ("only_lastname", CheckoutFormErrorMessages.ERROR_FIRST_NAME_REQUIRED),
        ("only_name", CheckoutFormErrorMessages.ERROR_LAST_NAME_REQUIRED),
        ("name_and_lastname", CheckoutFormErrorMessages.ERROR_POSTAL_CODE_REQUIRED)
    ])
    def test_checkout_form_errors \
                    (self, authentication_page, user_credentials, checkout_form_states, product_page, cart_page, checkout_page,
                     checkout_form_fill_out_type, expected_error):
        first_name, last_name, postal_code = checkout_form_states[checkout_form_fill_out_type]

        # GIVEN: The user is logged in the product page
        user, password = user_credentials["valid"]
        authentication_page.login(user, password)

        # AND: The user adds an element from the list to the cart
        add_product_to_cart_and_retrieve_its_info(product_page, "1", False)
        product_page.cart_icon.click()

        # WHEN: The user sends the checkout form
        cart_page.checkout_button.click()
        checkout_page.fill_checkout_form(first_name, last_name, postal_code)
        checkout_page.continue_button.click()

        # THEN: The user must see the proper error message indicating the missing checkout form fields
        expect(checkout_page.error_message).to_have_text(re.compile(f"^{expected_error}$", re.IGNORECASE))
