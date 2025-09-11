from pages.header_manu_cart import Header_manu_cart


class Checkout_overview_page(Header_manu_cart):
    def __init__(self,page):
        super().__init__(page)
    __FINISH = "#finish"

    def finish_order(self,):
        self.click(self.__FINISH)
        assert self.page_title() == "Checkout: Complete!", f"Error: Wrong title {self.page_title()}"
