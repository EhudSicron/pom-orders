from pages.header_manu_cart import Header_manu_cart


class Product_page(Header_manu_cart):
    def __init__(self,page):
        super().__init__(page)
    __ADD_TO_Cart = "#add-to-cart"

    def add_to_cart(self):
        self.click(self.__ADD_TO_Cart)
    def page_title(self):
        return self.get_text(self.__PRODUCT_TITLE)




