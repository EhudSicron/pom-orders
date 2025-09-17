import json

import allure
import pytest

from tests.basetest import Basetest

# @pytest.mark.usefixtures("setup_page_function")
class Test_7_relogin(Basetest):
#############   Main  ##############
    #@pytest.mark.usefixtures("setup_page_function")
    @allure.severity(severity_level=allure.severity_level.TRIVIAL)
    @allure.title("Test 07 relogin valid user")
    @allure.description("This test check the positive relogin scenario")
    @allure.story("Login")
    def test_07_login_valid_user(self,page):
        self.login_page.login("standard_user","secret_sauce")
        page_name = self.login_page.page_name()
        print(f"page name: {page_name}")
        assert self.products_page.page_title() == "Products", f"Error : {self.products_page.page_title()}"
        # Checkout menu logout
        self.checkout_page.open_menu()
        self.checkout_page.menu_logout()
        login = self.login_page.login_btn()
        assert  login == '', f"Error : {login}"
        self.login_page.login("standard_user", "secret_sauce")
        assert self.products_page.page_title() == "Products", f"Error : {self.products_page.page_title()}"

