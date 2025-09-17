import json
import allure
import pytest

from tests.basetest import Basetest

# @pytest.mark.usefixtures("setup_page_function")
class Test_1_login(Basetest):
#############   Main  ##############
    @allure.severity(severity_level=allure.severity_level.CRITICAL)
    @allure.title("Test 01 login valid user")
    @allure.description("This test check the positive login scenario")
    @allure.story("Login")
    def test_01_login_valid_user(self,page):
        print("Start test 1 - login")
        self.login_page.login("standard_user","secret_sauce")
        page_name = self.login_page.page_name()
        print(f"page name: {page_name}")
        print("End test 1 - login")
        assert self.products_page.page_title() == "Products", f"Error : {self.products_page.page_title()}"



