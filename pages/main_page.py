from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):

    HEADER = (By.CSS_SELECTOR, "[class*='utilityHeaderContainer']")

    def open(self):
        self.open_url('https://www.target.com/')

    def verify_header_present(self):
        self.find_element(*self.HEADER)



