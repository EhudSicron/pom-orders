from pages.header_menu_cart import HeaderMenuCart

class CheckoutOverviewPage(HeaderMenuCart):
    def __init__(self,page):
        super().__init__(page)
    __FINISH = "#finish"
    __LIST_PRODUCTS = ".cart_list>.cart_item"
    __PRODUCT_PRICE =".inventory_item_price"
    __TOTAL_PRICE = ".summary_subtotal_label"
    __TOTAL_PRICE_TAX = ".summary_total_label"
    __TAX = ".summary_tax_label"
    TAX_PRECENT = 8

    def finish_order(self):
        self.click(self.__FINISH)
        assert self.page_title() == "Checkout: Complete!", f"Error: Wrong title {self.page_title()}"

    def cal_sum_prices(self):
        sum_prod=0
        list_prod=self.page.locator(self.__LIST_PRODUCTS)
        count=list_prod.count()
        for i in range(count):
            text=self.get_text(list_prod.nth(i).locator(self.__PRODUCT_PRICE))
            text = text.replace("$","")
            tmp_price = self.get_price(text, "$", "$")
            if tmp_price >= 0:
                sum_prod += float(text)
        return sum_prod

    def get_price(self,price_text,text_remove1,text_remove2):
        price_text = price_text.replace(text_remove1, "")
        price_text = price_text.replace(text_remove2, "")
        if self.is_valid_int(price_text) or self.is_valid_float(price_text):
            price = float(price_text)
        else:
            price =-1
        return price

    def get_total_prices(self):
        total_price_text = self.get_text(self.__TOTAL_PRICE)
        total_price = self.get_price(total_price_text, "$", "Item total:")
        assert total_price >= 0 , f"Error total price is not a valid number = {total_price_text}"
        return total_price

    def get_tax(self):
        tax_text = self.get_text(self.__TAX)
        tax = self.get_price(tax_text, "$", "Tax:")
        assert tax >= 0 , f"Error total price with tax is not a valid number = {tax_text}"
        return tax

    def get_total_price_w_tax(self):
        total_price_tax_text = self.get_text(self.__TOTAL_PRICE_TAX)
        total_price_tax = self.get_price(total_price_tax_text, "$", "Total:")
        assert total_price_tax >= 0 , f"Error total price with tax is not a valid number = {total_price_tax_text}"
        return total_price_tax




