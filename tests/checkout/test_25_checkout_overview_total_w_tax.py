from multiprocessing.context import assert_spawning

import allure

from tests.basetest import Basetest


class Test_24_checkout_overview_tax_price(Basetest):
    @allure.severity(severity_level=allure.severity_level.NORMAL)
    @allure.title("test 24 checkout overview tax for total price")
    @allure.description("This test calc the tax for all products prices in the cart")
    @allure.story("Checkout")
    def test_24_checkout_overview_tax_price(self,page):
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
        total_prices = self.checkout_overview_page.get_total_prices()
        total_tax = self.checkout_overview_page.get_tax()
        total_price_w_tax = self.checkout_overview_page.get_total_price_w_tax()

        calc_total_with_tax = total_prices + total_tax
        assert calc_total_with_tax == round(total_price_w_tax,2), f"Error - total price after tax: {total_price_w_tax} is not equal to the calculated total+tax: {calc_total_with_tax} "




