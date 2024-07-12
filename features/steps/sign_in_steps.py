from selenium.webdriver.common.by import By
from behave import then
from time import sleep





@then('Verify Sign In form opened')
def verify_sign_in(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.XPATH, "//h1[.//span]").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'