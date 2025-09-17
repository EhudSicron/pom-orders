from multiprocessing.context import assert_spawning

import allure

from tests.basetest import Basetest


class Test_23_checkout_overview_sum_prices(Basetest):
    @allure.severity(severity_level=allure.severity_level.CRITICAL)
    @allure.title("test 23 checkout overview sum prices")
    @allure.description("This test check sum of all products prices in the checkout overview")
    @allure.story("Checkout")
    def test_23_checkout_overview_sum_prices(self,page):
        #############   Main  ##############
        # run login test
        self.login_page.login("standard_user","secret_sauce")
        # find Prod 1 and add to cart
        self.products_page.add_to_cart("Sauce Labs Bike Light")
        self.products_page.add_to_cart("Sauce Labs Backpack")
        count = self.products_page.cart_count()
        assert count==2, "Error wrong number of product in the cart"
        # checkout
        self.products_page.goto_cart()
        self.cart_page.checkout_cart()
        self.checkout_page.fill_user_add("Ehud","Sicron","123")
        self.checkout_page.continue_order()
        # Checkout overview
        sum_all_prices = self.checkout_overview_page.cal_sum_prices()
        total_price = self.checkout_overview_page.get_total_prices()
        assert total_price == round(sum_all_prices,2), f"Error - total price: {total_price} is not equal to the calculated sum: {sum_all_prices} "




