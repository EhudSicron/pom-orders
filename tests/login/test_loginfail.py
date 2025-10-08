import json

import allure
import pytest

from tests.basetest import Basetest


class TestLoginFail(Basetest):
    with open("tests\login_data.json", "r") as f:
        raw_data = json.load(f)
        test_data = [(d["username"], d["password"]) for d in raw_data]
    @pytest.mark.parametrize("user,password", test_data)
    @allure.severity(severity_level=allure.severity_level.NORMAL)
    @allure.title("Test 02 login fail - non-valid user")
    @allure.description("This test check the negative login scenario - wrong user and password")
    @allure.story("Login")
    def test_02_login_fail(self, user, password):
        log_test = "Start test 2 - login"
        # self.login_page.login("standard_user1","secret_sauce1")
        self.login_page.login(user, password)
        log_test = "End test 2 - login \n"
        #print("End test 2 - login")
        log_test += f"User:{user}, Password: {password}\n"
        #print(f"User:{user}, Password: {password}")
        error = self.login_page.error()
        #print(f"error:{error}")
        log_test += f"error:{error}\n"
        assert "Username and password do not match any user in this service" in error, f"Error is empty - login didn't fails : {error}\n User:{user}, Password: {password}"
