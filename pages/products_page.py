from pages.header_menu_cart import HeaderMenuCart


class ProductsPage(HeaderMenuCart):
    def __init__(self,page):
        super().__init__(page)
    __PRODUCT_LIST=".inventory_item"
    __PRODUCT_NAME=".inventory_item_name"
    __PRODUCT_SELECT="[id^='add-to-cart']"
    __PRODUCT_REMOVE = "[id^='remove-sauce']"
    __PRODUCT_SORT = ".product_sort_container"
    __PRODUCT_SORT_LIST = ".product_sort_container>option"
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

    def sort_products(self,sort_type):
        # sort options az,za,hilo,lohi
        self.hover(self.__PRODUCT_SORT)
        self.click(self.__PRODUCT_SORT)
        sort_list=self.page.locator(self.__PRODUCT_SORT)
        sort_type_value = "az"
        match  sort_type:
            case "az":
                sort_type_value="az"
                sort_type_active = "Name (A to Z)"
            case "za":
                sort_type_value="za"
                sort_type_active = "Name (Z to A)"
            case "lohi":
                sort_type_value="lohi"
                sort_type_active = "Price (low to high)"
            case "hilo":
                sort_type_value="hilo"
                sort_type_active = "Price (high to low)"
            case _:
                sort_type_value = "az"
                sort_type_active = "Name (A to Z)"
                print("Error wrong sort_type_value - default select az")
        sort_list.select_option(sort_type_value)
        print(f"Selected sort option: {self.get_text(".active_option")}")
        assert self.get_text(".active_option") == sort_type_active, f"Error fail - wrong sort option selected"

    def remove_from_cart(self, product_description):
        prodc_list=self.page.locator(self.__PRODUCT_LIST)
        count = prodc_list.count()
        print(count)
        for i in range(count):
            text = self.get_text(prodc_list.nth(i).locator(self.__PRODUCT_NAME))
            print(text)
            if text == product_description:
                print(f"Product name: {product_description}")
                self.click(prodc_list.nth(i).locator(self.__PRODUCT_REMOVE))
                break



