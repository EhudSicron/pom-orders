import allure

from tests.basetest import Basetest


class Test_20_cart_continue_shopping(Basetest):
    @allure.severity(severity_level=allure.severity_level.TRIVIAL)
    @allure.title("Test 20 cart continue shopping")
    @allure.description("This test check the return to products page - after clicks on continue shopping")
    @allure.story("Cart")
    def test_20_cart_continue_shoping(self):
        # run login test
        self.login_page.login("standard_user","secret_sauce")
        # find Prod 1 and add to cart
        self.products_page.go_to_product("Sauce Labs Bike Light")
        # go to cart
        self.product_page.add_to_cart()
        self.product_page.goto_cart()
        self.cart_page.continue_shopping()
        # checkout
        count = self.products_page.cart_count()
        assert count==1, f"Error wrong number of product in the cart should be 0 was: {count}"



