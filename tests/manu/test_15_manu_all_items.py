import allure

from tests.basetest import Basetest


class Test_15_manu_all_items(Basetest):
    @allure.severity(severity_level=allure.severity_level.NORMAL)
    @allure.title("Test 15 menu all items")
    @allure.description("This test open the manu and goes to all items - products page")
    @allure.story("Manu")
    def test_15_manu_all_items(self):
        # run login test
        self.login_page.login("standard_user","secret_sauce")
        # go to cart
        self.products_page.goto_cart()
        # Checkout menu all items
        self.checkout_page.open_menu()
        self.checkout_page.menu_all_items()



