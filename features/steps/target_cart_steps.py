from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a.sc-ab4ee1d1-1.sc-e487bf3b-0.bYXfno.fRitwa').click()
    sleep(4)

@then('Verify "Your cart is empty" message is shown')
def verify_cart_is_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    assert expected_text in actual_text, f'Expected {expected_text} ot in actual {actual_text}'