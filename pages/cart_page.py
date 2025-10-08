import allure

from pages.header_menu_cart import HeaderMenuCart

class CartPage(HeaderMenuCart):
    def __init__(self,page):
        super().__init__(page)

    __ADD_TO_Cart = "#add-to-cart"
    __PRODUCT_NAME = ".inventory_item_name"
    __PRODUCT_REMOVE= "[id^='remove-']"
    __CHECK_OUT = "#checkout"
    __CONTINUE_SHOP_BUT = "#continue-shopping"
    __CHECK_OUT_URL = "checkout-step-one.html"
    __CONTINUE_SHOP_URL = "inventory.html"
    __CART_LIST = ".cart_list>.cart_item"

    def remove_prod_from_cart(self, product_description):
        cart_list=self.page.locator(self.__CART_LIST)
        count = cart_list.count()
        log= f"cart items count:{count}\n"
        # print(count)
        remove_flag=False
        for i in range(count):
            text = self.get_text(cart_list.nth(i).locator(self.__PRODUCT_NAME))
            #print(text)
            log += str(text) + "\n"
            if text == product_description:
                #print(f"Product name: {product_description}")
                log += f"Product name: {product_description}\n"
                cart_list.nth(i).locator(self.__PRODUCT_REMOVE).click()
                remove_flag = True
                break
        allure.attach(body=log, name="text attachment", attachment_type=allure.attachment_type.TEXT)
        assert remove_flag == True , f"Remove product from cart fail: Product is not in the list {product_description}"

    def checkout_cart(self):
        self.page.locator(self.__CHECK_OUT).click()
        # print(f"self.page_url: {self.page_url()}")
        assert self.__CHECK_OUT_URL in self.page_url() , f"Move to checkout failed wrong page {self.page_url()}"

    def continue_shopping(self):
        self.page.locator(self.__CONTINUE_SHOP_BUT).click()
        assert self.__CONTINUE_SHOP_URL in self.page_url(), f"Move to CONTINUE_SHOP failed wrong page {self.page_url()}"



