from pages.header_menu_cart import HeaderMenuCart

class CheckoutPage(HeaderMenuCart):
    def __init__(self,page):
        super().__init__(page)
    __FIRST_NAME_FIELD="#first-name"
    __LAST_NAME_FIELD = "#last-name"
    __ZIP_FIELD="#postal-code"
    __CONTINUE= "#continue"
    __CANCEL = "#cancel"
    __CONTINUE_URL = "checkout-step-two.html"
    __CART_URL = "cart.html"

    def fill_user_add(self,first_name,last_name,zip_name):
        self.fill_text(self.__FIRST_NAME_FIELD,first_name)
        self.fill_text(self.__LAST_NAME_FIELD, last_name)
        self.fill_text(self.__ZIP_FIELD, zip_name)

    def continue_order(self,):
        self.click(self.__CONTINUE)
        assert self.__CONTINUE_URL in self.page_url(), f"Move to CONTINUE_SHOP failed wrong page {self.page_url()}"

    def cancel_order(self):
        self.click(self.__CANCEL)
        assert self.__CART_URL in self.page_url(), f"Cancel and move back to Cart failed wrong page {self.page_url()}"


