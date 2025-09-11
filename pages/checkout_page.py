from pages.header_manu_cart import Header_manu_cart


class Checkout_page(Header_manu_cart):
    def __init__(self,page):
        super().__init__(page)

    __FIRST_NAME_FIELD="#first-name"
    __LAST_NAME_FIELD = "#last-name"
    __ZIP_FIELD="#postal-code"
    __CONTINUE= "#continue"
    __CANCEL = "#cancel"



    def fill_user_add(self,first_name,last_name,zip_name):
        self.fill_text(self.__FIRST_NAME_FIELD,first_name)
        self.fill_text(self.__LAST_NAME_FIELD, last_name)
        self.fill_text(self.__ZIP_FIELD, zip_name)

    def continue_order(self,):
        self.click(self.__CONTINUE)
    def cancel_order(self):
        self.click(self.__CANCEL)

