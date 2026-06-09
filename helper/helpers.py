from playwright.sync_api import expect


def add_product_to_cart_and_retrieve_its_name(product_page, products_amount):
    random_item = product_page.pick_random_item()
    item_name = product_page.get_item_name(random_item)

    product_page.add_to_cart_an_item(random_item)

    expect(product_page.get_cart_counter()).to_have_text(products_amount)

    return item_name
