import json
import allure
import pytest

from tests.basetest import Basetest

# @pytest.mark.usefixtures("setup_page_function")
class TestLogin(Basetest):
#############   Main  ##############
    @allure.severity(severity_level=allure.severity_level.CRITICAL)
    @allure.title("Test 01 login valid user")
    @allure.description("This test check the positive login scenario")
    @allure.story("Login")
    def test_01_login_valid_user(self,page):
        log_test="Start test 1 - login \n"
        self.login_page.login("standard_user","secret_sauce")
        page_name = self.login_page.page_name()
        log_test+=f"page name: {page_name}\n"
        allure.attach(body=log_test, name="text attachment", attachment_type=allure.attachment_type.TEXT)
        assert self.products_page.page_title() == "Products", f"Error : {self.products_page.page_title()}"



