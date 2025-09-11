from pages.header_manu_cart import Header_manu_cart


class Login_page(Header_manu_cart):
    def __init__(self,page):
        super().__init__(page)

    __USER_NAME_FIELD= "#user-name"
    __PASSWORD_FIELD = "#password"
    __LOGIN_FIELD= "#login-button"
    __LOGIN_ERROR = ".error-message-container.error"


    def login(self,first_name,last_name):
        self.fill_text(self.__USER_NAME_FIELD,first_name)
        self.fill_text(self.__PASSWORD_FIELD, last_name)
        self.click(self.__LOGIN_FIELD)
    def error(self):
        return self.get_text(self.__LOGIN_ERROR)
    def login_btn(self):
        return self.get_text(self.__LOGIN_FIELD)




