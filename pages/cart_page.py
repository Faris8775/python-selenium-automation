from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    MUG_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='shippingButton']")
    ADD_MUG = (By.CSS_SELECTOR, '#addToCartButtonOrTextIdFor91283006')
    ADD_ITEM = (By.CSS_SELECTOR, "[data-test='modal-drawer-heading'] .h-text-lg")


    def open_cart(self):
        self.open_url('https://www.target.com/cart')


    def verify_cart_empty(self):
        self.wait_for_element_appear(*self.CART_EMPTY_MSG)
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_cart_items(self):
        cart_summary = self.find_element(*self.CART_SUMMARY).text
        self.verify_text(cart_summary, *self.CART_SUMMARY)

    def verify_product_name(self):
        product_name = self.find_element(*self.CART_ITEM_TITLE).text
        print(f'Actual product in cart name: {product_name}')
        self.verify_text(product_name, *self.CART_ITEM_TITLE)


    def add_mug_side_bar(self):
        self.wait_and_click(*self.MUG_SIDE_NAV)


    def add_mug(self):
        self.find_element(*self.ADD_MUG).click()


    def verify_item(self):
        expected_text = 'Added to cart'
        self.verify_text(expected_text, *self.ADD_ITEM)


