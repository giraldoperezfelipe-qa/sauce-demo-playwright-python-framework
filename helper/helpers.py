from playwright.sync_api import expect


def wait_for_element_to_be_visible(locator):
    locator.wait_for(state="visible")


def add_n_products_to_cart_and_retrieve_them(product_page, number_of_products_to_add):
    random_items_to_add = product_page.pick_random_n_products(number_of_products_to_add)
    product_page.add_items_to_cart(random_items_to_add)

    expect(product_page.get_cart_counter()).to_have_text(str(number_of_products_to_add))

    return random_items_to_add


def retrieve_names_from_products(products, item_name_locator):
    product_names_list = []

    for product in products:
        product_name = product.locator(item_name_locator).inner_text()
        product_names_list.append(product_name)

    return product_names_list


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
