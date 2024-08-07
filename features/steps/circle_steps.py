from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify the number of cells on Target Circle')
def verify_number_of_cells(context):
    # expected_result = 10
    # cells = context.driver.find_elements(By.CSS_SELECTOR, "div[class='cell-item-content']")
    # assert len(cells) == expected_result, f'Expected {expected_result} cells but got {len(cells)}'
    context.app.target_circle.verify_number_of_cells()


