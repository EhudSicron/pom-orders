import allure

from tests.basetest import Basetest


class TestMenuOptions(Basetest):
    @allure.severity(severity_level=allure.severity_level.NORMAL)
    @allure.title("Test 15 menu all items")
    @allure.description("This test open the menu and goes to all items - products page")
    @allure.story("Menu")
    def test_15_menu_all_items(self):
        # run login test
        self.login_page.login("standard_user","secret_sauce")
        # go to cart
        self.products_page.goto_cart()
        # Checkout menu all items
        self.checkout_page.open_menu()
        self.checkout_page.menu_all_items()

    @allure.severity(severity_level=allure.severity_level.NORMAL)
    @allure.title("Test 05 Open menu heder")
    @allure.description("This test open the header menu")
    @allure.story("Menu")
    def test_05_Menu_header(self):
        #############   Main  ##############
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

    @allure.severity(severity_level=allure.severity_level.NORMAL)
    @allure.title("Test 16 Open menu about")
    @allure.description("This test open the menu and goes to about page")
    @allure.story("Menu")
    def test_16_menu_about(self):
        #############   Main  ##############
        # run login test
        self.login_page.login("standard_user","secret_sauce")
        # Checkout menu about
        self.checkout_page.open_menu()
        self.checkout_page.menu_about()
        self.checkout_page.page.go_back()


