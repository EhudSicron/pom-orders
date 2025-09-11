from tests.basetest import Basetest


class Test_5_manu(Basetest):
    def test_5_manu(self):
        #############   Main  ##############
        print("Start test 5 - Manu")
        # run login test
        self.login_page.login("standard_user","secret_sauce")
        # find Prod 1 and add to cart
        # go to cart
        self.products_page.goto_cart()
        # checkout
        self.cart_page.checkout_cart()
        # Checkout menu about
        self.checkout_page.open_menu()
        self.checkout_page.menu_about()
        self.checkout_page.page.go_back()

        # Checkout menu all items
        self.checkout_page.open_menu()
        self.checkout_page.menu_all_items()

        # Go to cart checkout
        self.products_page.goto_cart()
        self.cart_page.checkout_cart()

        # Checkout menu logout
        self.checkout_page.open_menu()
        self.checkout_page.menu_logout()
        login = self.login_page.login_btn()
        assert  login == '', f"Error : {login}"
        print("End test 5 - Manu")

