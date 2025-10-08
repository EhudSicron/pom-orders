import allure

from tests.basetest import Basetest


class TestCheckoutCancel(Basetest):
    @allure.severity(severity_level=allure.severity_level.NORMAL)
    @allure.title("Test 04 checkout cancel order")
    @allure.description("This test add 2 products to cart, go to checkout and then cancel the order")
    @allure.story("Checkout")
    def Test_4_checkout_cancel(self):
        #############   Main  ##############
        # run login test
        self.login_page.login("standard_user","secret_sauce")

        # find Prod 1 and add to cart
        self.products_page.go_to_product("Sauce Labs Bike Light")
        self.product_page.add_to_cart()
        self.product_page.page.go_back()
        # go to cart
        self.products_page.goto_cart()
        self.cart_page.remove_prod_from_cart("Sauce Labs Backpack")
        # checkout
        self.cart_page.checkout_cart()
        self.checkout_page.cancel_order()
        assert self.cart_page.page_title()=="Your Cart", "The cancel fail - wrong page"


