import allure

from tests.basetest import Basetest


class Test_21_checkout_checkout(Basetest):
    @allure.severity(severity_level=allure.severity_level.TRIVIAL)
    @allure.title("Test 20 cart continue shopping")
    @allure.description("This test check the return to products page - after clicks on continue shopping")
    @allure.story("Checkout")
    def test_21_checkout_checkout(self):
        # run login test
        self.login_page.login("standard_user","secret_sauce")
        # find Prod 1 and add to cart
        self.products_page.go_to_product("Sauce Labs Bike Light")
        # go to cart
        self.product_page.add_to_cart()
        self.product_page.goto_cart()
        # checkout
        self.cart_page.checkout_cart()
        self.checkout_page.fill_user_add("Ehud","Sicron","112233")
        self.checkout_page.continue_order()




