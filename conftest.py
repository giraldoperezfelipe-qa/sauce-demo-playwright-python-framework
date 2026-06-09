import allure
import pytest
from playwright.sync_api import Page
from pages.authentication_page import AuthenticationPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pathlib import Path


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed and "page" in item.funcargs:
        page = item.funcargs["page"]
        path = Path("allure-results") / f"{item.name}.png"
        page.screenshot(path=str(path))
        allure.attach.file(
            str(path),
            name=path.name,
            attachment_type=allure.attachment_type.PNG,
        )


@pytest.fixture
def authentication_page(page: Page):
    return AuthenticationPage(page)


@pytest.fixture
def product_page(page: Page):
    return ProductPage(page)

@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)


@pytest.fixture
def user_credentials():
    standard_user = "standard_user"
    secret_sauce = "secret_sauce"
    blank_string = ""

    return {
        "valid": (standard_user, secret_sauce),
        "invalid": ("qwerty123", "qwerty9685"),
        "blank_credentials": (blank_string, blank_string),
        "blank_username": (blank_string, secret_sauce),
        "blank_password": (standard_user, blank_string),
        "locked": ("locked_out_user", secret_sauce),
    }
