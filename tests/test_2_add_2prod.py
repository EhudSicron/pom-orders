from tests.basetest import Basetest


class Test_2_add_2prod(Basetest):
    def test_2_add_2prod(self,page):
        #############   Main  ##############
        print("Start test 2 - add 2 products")
        # run login test
        self.login_page.login("standard_user","secret_sauce")
        # find Prod 1 and add to cart

        self.products_page.go_to_product("Sauce Labs Bike Light")
        self.product_page.add_to_cart()
        # ---Ehud error ------------- self.product_page.page.go_back()
        # find Prod 2 and add to cart
        self.products_page.go_to_product("Sauce Labs Backpack")
        self.product_page.add_to_cart()
        page.go_back()

        # go to cart
        self.products_page.goto_cart()
        count = self.cart_page.cart_count()
        assert count==2, "Error wrong number of product in the cart"
        # checkout
        self.cart_page.checkout_cart()
        self.checkout_page.fill_user_add("Ehud","Sicron","123")
        self.checkout_page.continue_order()
        # Checkout overview
        self.checkout_overview_page.open_menu()
        self.checkout_overview_page.menu_about()
        self.checkout_overview_page.page.go_back()
        self.checkout_overview_page.finish_order()
        print("End test 2 - add 2 products")

