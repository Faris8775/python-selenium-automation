from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click Sign In')
def main_sign_in(context):
    # click the sign in on main page
    context.driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()
    # wait for the SignIn sidebar to load
    sleep(2)

@when('From right side navigation menu, click Sign In')
def side_sign_in(context):
    # click the side nav sign in
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']").click()
    # wait for the SignIn sidebar to load
    sleep(4)

@then('Verify Sign In form opened')
def verify_sign_in(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.XPATH, "//h1[.//span]").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'