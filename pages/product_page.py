from pages.header_menu_cart import HeaderMenuCart

class ProductPage(HeaderMenuCart):
    def __init__(self,page):
        super().__init__(page)
    __ADD_TO_CART = "#add-to-cart"
    __REMOVE_FROM_CART = "#remove"
    __Back_to_products = "#back-to-products"
    __PRODUCTS_URL = "inventory.html"

    def add_to_cart(self):
        self.click(self.__ADD_TO_CART)

    def remove_from_cart(self):
        self.click(self.__REMOVE_FROM_CART)

    def page_title(self):
        return self.get_text(self.__PRODUCT_TITLE)

    def back_to_products(self):
        self.click(self.__Back_to_products)
        assert self.__PRODUCTS_URL in self.page_url(), f"Error the Move to PRODUCTS page failed wrong page {self.page_url()}"




