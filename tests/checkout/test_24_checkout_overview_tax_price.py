from multiprocessing.context import assert_spawning

import allure

from tests.basetest import Basetest


class Test_24_checkout_overview_tax_price(Basetest):
    @allure.severity(severity_level=allure.severity_level.CRITICAL)
    @allure.title("test 23 checkout overview tax for total price")
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
        total_price = self.checkout_overview_page.get_total_prices()
        tax = self.checkout_overview_page.get_tax()
        tax_precent = self.checkout_overview_page.TAX_PRECENT
        calc_tax = round(total_price* (self.checkout_overview_page.TAX_PRECENT/100),2)

        assert tax == calc_tax, f"Error - total price: {tax} is not equal to the calculated tax: {calc_tax} "




