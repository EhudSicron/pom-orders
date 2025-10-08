from typing import Dict
from time import sleep

import allure
import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.products_page import ProductsPage
from tests.config import ConfigReader
from allure_commons.types import AttachmentType


@pytest.fixture(scope="class")
def setup_page_class(request, browser):
    print("SETUP #####################  SETUP ###########")
    request.cls.page = browser.new_page()
    request.cls.page.goto("http://www.saucedemo.com")
    request.cls.login_page= LoginPage(request.cls.page)
    request.cls.cart_page = CartPage(request.cls.page)
    request.cls.checkout_overview_page = CheckoutOverviewPage(request.cls.page)
    request.cls.checkout_page = CheckoutPage(request.cls.page)
    request.cls.product_page = ProductPage(request.cls.page)
    request.cls.products_page = ProductsPage(request.cls.page)
    request.cls.sleep = sleep
    yield
    sleep(3)
    request.cls.page.close()
    browser.close()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "no_viewport": True,
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: Dict):
    """Fixture to set browser launch arguments.
    Args:
        browser_type_launch_args (dict): Browser type launch arguments.
    Returns:
        dict: Updated browser type launch arguments.
    See Also:
        https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch
    """
    return {**browser_type_launch_args, "args": ["--start-maximized"]}


@pytest.fixture(scope="function",autouse=True) #,
def setup_page_function(request, page: Page):
    print("SETUP #####################  SETUP ###########")
    url = ConfigReader.read_config('general','url')
    #page.goto("http://www.saucedemo.com")
    page.goto(url)
    request.cls.login_page= LoginPage(page)
    request.cls.cart_page = CartPage(page)
    request.cls.checkout_overview_page = CheckoutOverviewPage(page)
    request.cls.checkout_page = CheckoutPage(page)
    request.cls.product_page = ProductPage(page)
    request.cls.products_page = ProductsPage(page)
    yield
    sleep(2)


