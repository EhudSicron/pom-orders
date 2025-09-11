from pages.header_manu_cart import Header_manu_cart


class Products_page(Header_manu_cart):
    def __init__(self,page):
        super().__init__(page)

    __PRODUCT_LIST=".inventory_item"
    __PRODUCT_NAME=".inventory_item_name"
    __PRODUCT_SELECT="[id^='add-to-cart']"
    #__PRODUCT_TITLE = ".header_secondary_container>.title"

    def add_to_cart(self, product_description):
        prodc_list=self.page.locator(self.__PRODUCT_LIST)
        count = prodc_list.count()
        print(count)
        for i in range(count):
            text = self.get_text(prodc_list.nth(i).locator(self.__PRODUCT_NAME))
            print(text)
            if text == product_description:
                print(f"Product name: {product_description}")
                self.click(prodc_list.nth(i).locator(self.__PRODUCT_SELECT))
                break
    def go_to_product(self, product_description):
        prodc_list=self.page.locator(self.__PRODUCT_LIST)
        count = prodc_list.count()
        print(count)
        for i in range(count):
            text = self.get_text(prodc_list.nth(i).locator(self.__PRODUCT_NAME))
            if text == product_description:
                print(f"Product name: {product_description}")
                self.click(prodc_list.nth(i).locator(self.__PRODUCT_NAME))
                break
    def page_name(self):
        return self.page_name()




