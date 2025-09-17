import allure

from tests.basetest import Basetest


class Test_16_manu_about(Basetest):
    @allure.severity(severity_level=allure.severity_level.NORMAL)
    @allure.title("Test 16 Open manu about")
    @allure.description("This test open the manu and goes to about page")
    @allure.story("Manu")
    def test_16_manu_about(self):
        #############   Main  ##############
        print("Start test 5 - Manu")
        # run login test
        self.login_page.login("standard_user","secret_sauce")
        # Checkout menu about
        self.checkout_page.open_menu()
        self.checkout_page.menu_about()
        self.checkout_page.page.go_back()

