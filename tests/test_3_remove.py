from tests.basetest import Basetest


class Test_3_remove(Basetest):
    def test_3_remove(self):
        #############   Main  ##############
        print("Start test 3 - remove products")
        # run login test
        self.login_page.login("standard_user","secret_sauce")
        # find Prod 1 and add to cart
        self.products_page.go_to_product("Sauce Labs Bike Light")
        self.product_page.add_to_cart()
        self.product_page.page.go_back()
        # find Prod 2 and add to cart
        self.products_page.go_to_product("Sauce Labs Backpack")
        self.product_page.add_to_cart()
        self.product_page.page.go_back()
        # go to cart
        self.products_page.goto_cart()
        self.cart_page.remove_prod_from_cart("Sauce Labs Backpack")
        self.cart_page.remove_prod_from_cart("Sauce Labs Bike Light")
        # checkout
        count = self.cart_page.cart_count()
        assert count==0, f"Error wrong number of product in the cart should be 0 was: {count}"
        self.cart_page.checkout_cart()

        print("End test 3 - remove products")

