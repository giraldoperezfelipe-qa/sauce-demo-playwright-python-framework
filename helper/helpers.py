from playwright.sync_api import expect


def add_n_products_to_cart(product_page, number_of_products_to_add):
    random_items_to_add = product_page.pick_random_n_products(number_of_products_to_add)
    product_page.add_items_to_cart(random_items_to_add)

    expect(product_page.get_cart_counter()).to_have_text(str(number_of_products_to_add))

def wait_for_element_to_be_visible(locator):
    locator.wait_for(state="visible")