import allure

from tests.basetest import Basetest


class TestMenuFlow(Basetest):
    @allure.severity(severity_level=allure.severity_level.NORMAL)
    @allure.title("Test 17 Open menu flow")
    @allure.description("This test all menu options")
    @allure.story("Menu")
    def test_17_menu_flow(self):
        # run login test
        self.login_page.login("standard_user","secret_sauce")
        # go to cart
        self.products_page.goto_cart()
        # checkout
        self.cart_page.checkout_cart()
        # Checkout menu about
        self.checkout_page.open_menu()
        self.checkout_page.menu_about()
        self.checkout_page.page.go_back()

        # Checkout menu all items
        self.checkout_page.open_menu()
        self.checkout_page.menu_all_items()

        # Go to cart checkout
        self.products_page.goto_cart()
        self.cart_page.checkout_cart()

        # Checkout menu logout
        self.checkout_page.open_menu()
        self.checkout_page.menu_logout()
        login = self.login_page.login_btn()
        assert  login == '', f"Error : {login}"

