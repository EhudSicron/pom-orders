import allure

from tests.basetest import Basetest


class Test_19_product_remove(Basetest):
    @allure.severity(severity_level=allure.severity_level.TRIVIAL)
    @allure.title("Test 19 remove products from cart in product page")
    @allure.description("This test check the removal of products from the cart in product page - verify cart has 2 less products")
    @allure.story("Products")
    def test_19_product_remove(self):
        #############   Main  ##############
        print("Start test 6 - remove products")
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
        count = self.cart_page.cart_count()
        assert count == 2, f"Error wrong number of product in the cart should be 2 was: {count}"
        # remove products
        self.products_page.go_to_product("Sauce Labs Bike Light")
        self.product_page.remove_from_cart()
        self.product_page.back_to_products()
        self.products_page.go_to_product("Sauce Labs Backpack")
        self.product_page.remove_from_cart()

        # checkout
        count = self.product_page.cart_count()
        assert count==0, f"Error wrong number of product in the cart should be 0 was: {count}"




