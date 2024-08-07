from selenium.webdriver.common.by import By
from behave import then
from time import sleep



@when('Open cart page')
def open_cart(context):
    context.app.cart_page.open_cart()

@when('Add a mug to cart on side bar')
def add_mug_side_bar(context):
    context.app.cart_page.add_mug_side_bar()


@when('Add a mug to cart')
def add_mug(context):
    context.app.cart_page.add_mug()




@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.verify_product_name()

@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.app.cart_page.verify_cart_items()

@then('Verify item in cart')
def verify_item(context):
    context.app.cart_page.verify_item()

@then('Verify "Your cart is empty" message is shown')
def verify_cart_is_empty(context):
    context.app.cart_page.verify_cart_empty()