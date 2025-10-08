import allure

from tests.basetest import Basetest


class TestCartRemove(Basetest):
    @allure.severity(severity_level=allure.severity_level.TRIVIAL)
    @allure.title("Test 06 remove products from cart")
    @allure.description("This test check the removal of products from the cart - verify cart has 2 less products")
    @allure.story("Cart")
    def test_6_cart_remove(self):
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



