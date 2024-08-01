from selenium.webdriver.common.by import By

from pages.base_page import Page

class SignInPage(Page):

    SIGN_IN = (By.XPATH, "//h1[.//span]")

    def verify_sign_in(self):
        expected_text = 'Sign into your Target account'
        self.verify_text(expected_text, *self.SIGN_IN)


