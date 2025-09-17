import json

import allure
import pytest

from tests.basetest import Basetest

class Test_8_login_user_locked(Basetest):
    # @pytest.mark.usefixtures("setup_page_function")
    test_data=[("locked_out_user","secret_sauce")]
    @pytest.mark.parametrize("user,password", test_data)
    @allure.severity(severity_level=allure.severity_level.NORMAL)
    @allure.title("Test 08 login locked user")
    @allure.description("This test check the negative login scenario - locked with correct user and password")
    @allure.story("Login")
    def Test_08_login_user_locked(self, user, password):
        # self.login_page.login("standard_user1","secret_sauce1")
        self.login_page.login(user, password)
        print(f"User:{user}, Password: {password}")
        error = self.login_page.error()
        print(f"error:{error}")
        assert "Sorry, this user has been locked out" in error, f"Wrong Error  - user is not locked - fails : {error}\\n User:{user}, Password: {password}"
