import allure

from tests.basetest import Basetest


class Test_13_sort_lohi(Basetest):
    @allure.severity(severity_level=allure.severity_level.TRIVIAL)
    @allure.title("Test 13 hilo sort products list")
    @allure.description("This test check the sorting the products page according to hilo")
    @allure.story("Products")
    def test_10_sort_za(self,page):
        #############   Main  ##############
        # run login test
        self.login_page.login("standard_user","secret_sauce")
        # find Prod 1 and add to cart
        self.products_page.sort_products("hilo")