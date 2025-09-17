import json

import allure
import pytest

from tests.basetest import Basetest

class Test_9_login_logout(Basetest):
    @allure.severity(severity_level=allure.severity_level.TRIVIAL)
    @allure.title("Test 9 logout valid user")
    @allure.description("This test check the positive logout scenario")
    @allure.story("Login")
    def test_09_login_valid_user(self,page):
        self.login_page.login("standard_user","secret_sauce")
        page_name = self.login_page.page_name()
        print(f"page name: {page_name}")
        assert self.products_page.page_title() == "Products", f"Error : {self.products_page.page_title()}"
        # Checkout menu logout
        self.checkout_page.open_menu()
        self.checkout_page.menu_logout()
        login = self.login_page.login_btn()
        assert  login == '', f"Error : {login}"

