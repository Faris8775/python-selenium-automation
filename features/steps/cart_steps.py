from selenium.webdriver.common.by import By
from behave import then
from time import sleep



@when('Add a mug to cart')
def add_mug(context):
    context.driver.find_element(By.CSS_SELECTOR, '#addToCartButtonOrTextIdFor91283006').click()

@when('Add a mug to cart on side bar')
def add_mug_side_bar(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='shippingButton']").click()


@then('Verify item in cart')
def verify_item(context):
    expected_text = 'Added to cart'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='modal-drawer-heading'] .h-text-lg").text
    assert expected_text in actual_text, f'Expected {expected_text} ot in actual {actual_text}'

@then('Verify "Your cart is empty" message is shown')
def verify_cart_is_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    assert expected_text in actual_text, f'Expected {expected_text} ot in actual {actual_text}'