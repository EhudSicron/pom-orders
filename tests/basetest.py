from pages.cart_page import Cart_page
from pages.checkout_overview_page import Checkout_overview_page
from pages.checkout_page import Checkout_page
from pages.login_page import Login_page
from pages.product_page import Product_page
from pages.products_page import Products_page
from time import sleep

class Basetest:
    login_page: Login_page
    cart_page: Cart_page
    checkout_overview_page: Checkout_overview_page
    checkout_page: Checkout_page
    product_page: Product_page
    products_page: Products_page
    sleep: sleep


