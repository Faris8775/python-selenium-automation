from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    MAIN_SIGN_IN = (By.XPATH, "//a[@aria-label='Account, sign in']")
    SIDE_SIGN_IN = (By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']")


    def search_product(self, product):
        print('POM layer:', product)
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        # wait for the page with search results to load
        sleep(6)

    def click_cart(self):
        self.wait_and_click(*self.CART_BTN)

    def main_sign_in(self):
        self.wait_and_click(*self.MAIN_SIGN_IN)

    def side_sign_in(self):
        self.wait_and_click(*self.SIDE_SIGN_IN)

