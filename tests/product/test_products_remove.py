import allure

from tests.basetest import Basetest


class TestProductsRemove(Basetest):
    @allure.severity(severity_level=allure.severity_level.TRIVIAL)
    @allure.title("Test 18 remove products from cart in products page")
    @allure.description("This test check the removal of products from the cart in products page - verify cart has 2 less products")
    @allure.story("Products")
    def test_18_products_remove(self):
        #############   Main  ##############
        # run login test
        self.login_page.login("standard_user","secret_sauce")
        # find Prod 1 and add to cart
        self.products_page.add_to_cart("Sauce Labs Bike Light")
        # find Prod 2 and add to cart
        self.products_page.add_to_cart("Sauce Labs Backpack")
        count = self.products_page.cart_count()
        assert count == 2, f"Error wrong number of product in the cart should be 2 was: {count}"
        # remove products
        self.products_page.remove_from_cart("Sauce Labs Backpack")
        self.products_page.remove_from_cart("Sauce Labs Bike Light")
        # checkout
        count = self.products_page.cart_count()
        assert count==0, f"Error wrong number of product in the cart should be 0 was: {count}"


