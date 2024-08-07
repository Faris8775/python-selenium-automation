from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")

    FAVORITES_BTN = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAVORITES_TOOLTIP_TXT = (By.XPATH, "//*[text()='Click to sign in and save']")
    LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
    PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")


    def hover_fav_icon(self):
        # fav_icon = self.find_element(*self.FAVORITES_BTN)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(fav_icon)
        # actions.perform()
        self.wait_for_element_appear(*self.FAVORITES_BTN)
        self.hover_element(*self.FAVORITES_BTN)

    def verify_fav_tooltip(self):
        self.wait_for_element_appear(*self.FAVORITES_TOOLTIP_TXT)

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT)

    def verify_product_in_url(self, expected_product):
        self.verify_partial_url(expected_product)

    def verify_product_name_img(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(4)
        self.driver.execute_script("window.scrollBy(0,2000)", "")

        all_products = self.driver.find_elements(*self.LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

        for product in all_products:
            title = product.find_element(*self.PRODUCT_TITLE).text
            assert title, 'Product title not shown'
            print(title)
            product.find_element(*self.PRODUCT_IMG)

    def click_add_to_cart(self):
        self.wait_and_click(*self.ADD_TO_CART_BTN)
        self.wait_for_element_appear(*self.SIDE_NAV_PRODUCT_NAME)

    def store_product_name(self):
        product_name = self.find_element(*self.SIDE_NAV_PRODUCT_NAME)
        print(f'Product stored: {product_name}')

    def side_nav_click_add_to_cart(self):
        self.wait_until_clickable(*self.SIDE_NAV_ADD_TO_CART_BTN)


