from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    MAIN_SIGN_IN = (By.XPATH, "//a[@aria-label='Account, sign in']")
    SIDE_SIGN_IN = (By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']")
    LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")
    TARGET_CIRCLE = (By.CSS_SELECTOR, '#utilityNav-circle')

    def verify_header_link_amount(self, number):
        number = int(number)   # convert str "6" ==> to int 6
        links = self.find_elements(*self.LINKS)
        assert len(links) == number, f'Expected {number} links but got {len(links)}'
        # Make sure to always assert len() for multiple elements as shown above
        # because .find_elements() function never fails.

    def verify_click_links(self):
        links = self.find_elements(*self.LINKS)

        for i in range(len(links)):
            # Search for links again because their internal IDs changed:
            # to avoid Stale Element Exception
            links = self.find_elements(*self.LINKS)
            print(f'Clicking on link {links[i].text}')
            links[i].click()
            sleep(4)


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

    def open_target_circle(self):
        self.wait_and_click(*self.TARGET_CIRCLE)