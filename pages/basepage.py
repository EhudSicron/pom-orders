from time import sleep

from playwright.sync_api import Page,Locator


class BasePage:
    """ Wrapper for Playwright operations """

    def __init__(self, page: Page):
        self.page = page


    def click(self, locator_or_selector) -> None:
        sleep(1)
        if isinstance(locator_or_selector, Locator):
            locator_or_selector.highlight()
            locator_or_selector.click()
        else:
            self.page.locator(locator_or_selector).highlight()
            self.page.locator(locator_or_selector).click()
        print(self.page.url)
        sleep(0.5)

    def hover(self, locator) -> None:
        sleep(1)
        self.page.locator(locator).hover()

    def fill_text(self, locator, txt: str) -> None:
        self.page.locator(locator).highlight()
        self.page.locator(locator).fill(txt)

    def get_text(self, locator_or_selector) -> str:
        if isinstance(locator_or_selector, Locator):
            if locator_or_selector.is_visible():
                locator_or_selector.highlight()
                text = locator_or_selector.inner_text()
            else:
                text = "Error: attribute is not available"
        else:
            if self.page.locator(locator_or_selector).is_visible():
                self.page.locator(locator_or_selector).highlight()
                text = self.page.locator(locator_or_selector).inner_text()
            else:
                text = "Error: attribute is not available"
        return text
    def page_name(self):
        return self.page.title()
    def page_url(self):
        print(f"page url")
        print(f"page url{self.page.url}")
        return self.page.url

    def is_valid_float(self,s):
        try:
            # Attempt to convert the string to a float
            float(s)
            return True
        except ValueError:
            # If a ValueError is raised, the conversion failed
            return False
    def is_valid_int(self,s):
        try:
            # Attempt to convert the string to a float
            int(s)
            return True
        except ValueError:
            # If a ValueError is raised, the conversion failed
            return False

