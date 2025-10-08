from pages.base_page import BasePage


class HeaderMenuCart(BasePage):
    def __init__(self,page):
        super().__init__(page)
    __Cart = ".shopping_cart_link"
    __MENU = "#react-burger-menu-btn"
    __ALL_ITEMS = "#inventory_sidebar_link "
    __ABOUT = "#about_sidebar_link"
    __LOGOUT = "#logout_sidebar_link"
    __RESET_APP = "#reset_sidebar_link"
    __PRODUCT_TITLE = ".header_secondary_container>.title"
    __CLOSE_MENU = "#react-burger-cross-btn"
    __CART_URL = "cart.html"
    __All_ITEMS_URL = "inventory.html"
    __ABOUT_URL = "https://saucelabs.com/"
    __LOGIN_BUT = "#login-button"
    __CART_PRODUCT = ".shopping_cart_link"
    __CART_PRODUCT_NUM = ".shopping_cart_badge"
    __PRODUCTS_LIST = ".cart_item"

    def goto_cart(self):
        self.page.locator(self.__Cart).click()
        assert self.__CART_URL in self.page_url(), f"Cancel and move back to Cart failed wrong page {self.page_url()}"

    def open_menu(self):
        self.hover(self.__MENU)
        self.click(self.__MENU)
        assert self.page.locator(self.__ALL_ITEMS).is_visible(), f"Open Menu failed - ALL_ITEMS is not visible"

    def menu_all_items(self):
        self.click(self.__ALL_ITEMS)
        assert self.__All_ITEMS_URL in self.page_url(), f"Move to All Items failed wrong page {self.page_url()}"

    def menu_about(self):
        self.click(self.__ABOUT)
        assert self.__ABOUT_URL == self.page_url(), f"Move to About main page failed {self.page_url()}"

    def menu_logout(self):
        self.click(self.__LOGOUT)
        assert self.page.locator(self.__LOGIN_BUT).is_visible(), f"Move to logout page failed - Login button is not visible"

    def menu_reset_app(self):
        self.click(self.__RESET_APP)
        num_prod_in_cart = self.get_text("__CART_PRODUCT_NUM")
        assert num_prod_in_cart == '0', f"Reset App fail - num products in cart is not 0, num product = {num_prod_in_cart}  "

    def page_title(self):
        return self.get_text(self.__PRODUCT_TITLE)

    def close_menu(self):
         self.click(self.__CLOSE_MENU)
         assert self.page.locator(self.__ALL_ITEMS).is_visible(), f"Close Menu failed - ALL_ITEMS is visible"

    def cart_count(self):
        if self.page.locator(self.__CART_PRODUCT).is_visible():
            if self.page.locator(self.__CART_PRODUCT_NUM).is_visible():
                num_prod_in_cart = self.get_text(self.__CART_PRODUCT_NUM)
            else:
                num_prod_in_cart='0'
        else:
            num_prod_in_cart = '0'
            assert num_prod_in_cart=='0' , f"Error - the {self.__CART_PRODUCT} is not visible"
        return int(num_prod_in_cart)
