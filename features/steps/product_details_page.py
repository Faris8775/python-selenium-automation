from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


# COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li")
# SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.app.product_page.open_product(product_id)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    context.app.product_page.click_and_verify_colors()


