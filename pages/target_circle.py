from selenium.webdriver.common.by import By

from pages.base_page import Page


class TargetCircle(Page):

    CELLS = (By.CSS_SELECTOR, "div[class='cell-item-content']")


    def verify_number_of_cells(self):
        expected_result = 10
        cells = self.find_elements(*self.CELLS)
        assert len(cells) == expected_result, f'Expected {expected_result} cells but got {len(cells)}'