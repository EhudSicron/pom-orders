from pages.basepage import BasePage


class Header_manu_cart(BasePage):
    def __init__(self,page):
        super().__init__(page)

    __Cart = ".shopping_cart_link"
    __MENU = "#react-burger-menu-btn"
    __ALL_ITEMS = "#inventory_sidebar_link"
    __ABOUT = "#about_sidebar_link"
    __LOGOUT = "#logout_sidebar_link"
    __RESET_APP = "#reset_sidebar_link"
    __PRODUCT_TITLE = ".header_secondary_container>.title"

    def goto_cart(self):
        self.page.locator(self.__Cart).click()

    def open_menu(self):
        self.hover(self.__MENU)
        self.click(self.__MENU)

    def menu_all_items(self):
        self.click(self.__ALL_ITEMS)

    def menu_about(self):
        self.click(self.__ABOUT)

    def menu_logout(self):
        self.click(self.__LOGOUT)

    def menu_reset_app(self):
        self.click(self.__RESET_APP)

    def page_title(self):
        return self.get_text(self.__PRODUCT_TITLE)
