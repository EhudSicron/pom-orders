from pages.cart_page import CartPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.products_page import ProductsPage
from time import sleep



class Basetest:
    login_page: LoginPage
    cart_page: CartPage
    checkout_overview_page: CheckoutOverviewPage
    checkout_page: CheckoutPage
    product_page: ProductPage
    products_page: ProductsPage
    sleep: sleep





