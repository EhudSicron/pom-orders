import allure

from tests.basetest import Basetest


class Test_5_manu_header(Basetest):
    @allure.severity(severity_level=allure.severity_level.NORMAL)
    @allure.title("Test 05 Open manu heder")
    @allure.description("This test open the header manu")
    @allure.story("Manu")
    def test_05_manu_header(self):
        #############   Main  ##############
        print("Start test 5 - Manu")
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



