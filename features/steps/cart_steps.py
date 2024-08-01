from selenium.webdriver.common.by import By
from behave import then
from time import sleep

CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')

@when('Add a mug to cart on side bar')
def add_mug_side_bar(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='shippingButton']").click()

@when('Add a mug to cart')
def add_mug(context):
    context.driver.find_element(By.CSS_SELECTOR, '#addToCartButtonOrTextIdFor91283006').click()




@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Actual product in cart name: {actual_name}')
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then('Verify item in cart')
def verify_item(context):
    expected_text = 'Added to cart'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='modal-drawer-heading'] .h-text-lg").text
    assert expected_text in actual_text, f'Expected {expected_text}  in actual {actual_text}'

@then('Verify "Your cart is empty" message is shown')
def verify_cart_is_empty(context):
    context.app.cart_page.verify_cart_empty()