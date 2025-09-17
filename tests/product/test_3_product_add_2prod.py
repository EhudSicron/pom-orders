import allure

from tests.basetest import Basetest


class Test_03_product_add_2prod(Basetest):
    @allure.severity(severity_level=allure.severity_level.CRITICAL)
    @allure.title("Test 03 add 2 products")
    @allure.description("This test check the adding 2 products to cart from products page - verify cart has 2 more products")
    @allure.story("Products")
    def test_03_product_add_2prod(self,page):
        #############   Main  ##############
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
        count = self.cart_page.cart_count()
        assert count==2, "Error wrong number of product in the cart"
        # checkout
        self.cart_page.checkout_cart()
        self.checkout_page.fill_user_add("Ehud","Sicron","123")
        self.checkout_page.continue_order()
        # Checkout overview
        self.checkout_overview_page.finish_order()


