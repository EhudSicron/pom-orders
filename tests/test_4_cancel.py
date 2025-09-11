from tests.basetest import Basetest


class Test_4_cancel(Basetest):
    def test_4_cancel(self):
        #############   Main  ##############
        print("Start test 4 - Cancel")
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
        print("End test 4 - cancel order")

