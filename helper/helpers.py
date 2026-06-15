from playwright.sync_api import expect


def add_product_to_cart_and_retrieve_its_info \
                (product_page, products_amount, retrieve_its_info):
    random_item = product_page.pick_random_item()
    item_info = None

    # Get the item info, only if retrieve_its_info = true
    if retrieve_its_info:
        item_info = (product_page.get_item_name(random_item), product_page.get_item_description(random_item))

    product_page.add_to_cart_an_item(random_item)
    expect(product_page.get_cart_counter()).to_have_text(products_amount)

    # Return the item info, only if retrieve_its_info = true
    if retrieve_its_info:
        return item_info
    else:
        return None
