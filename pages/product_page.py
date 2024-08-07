from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class ProductPage(Page):

    COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li")
    SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

    def open_product(self, product_id):
        self.open_url(f'https://www.target.com/p/{product_id}')
        sleep(8)

    def click_and_verify_colors(self):
        expected_colors = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
        actual_colors = []

        colors = self.find_elements(*self.COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
        for color in colors[:4]:
            color.click()

            selected_color = self.find_element(*self.SELECTED_COLOR).text  # 'Color\nBlack'
            print('Current color', selected_color)

            selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
            actual_colors.append(selected_color)
            print(actual_colors)

        assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'