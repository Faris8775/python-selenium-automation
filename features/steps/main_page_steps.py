from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
MAIN_SIGN_IN = (By.XPATH, "//a[@aria-label='Account, sign in']")
SIDE_SIGN_IN = (By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']")
SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")


@given('Open target main page')
def open_target(context):
    context.app.main_page.open()

@when('Click Target Circle page')
def open_target_circle(context):
    context.driver.find_element(By.CSS_SELECTOR, '#utilityNav-circle').click()


@when('Search for product')
def search_product(context):
    context.app.header.search_product()

@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable(*CART_ICON)).click()



@when('Click Sign In')
def main_sign_in(context):
    # click the sign in on main page
    context.driver.wait.until(EC.element_to_be_clickable(MAIN_SIGN_IN)).click()
    # wait for the SignIn sidebar to load
    # sleep(2)

@when('From right side navigation menu, click Sign In')
def side_sign_in(context):
    # click the side nav sign in
    context.driver.wait.until(EC.element_to_be_clickable(SIDE_SIGN_IN)).click()
    # wait for the SignIn sidebar to load
    # sleep(4)


@when('Search for {product}')
def search_product(context, product):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # click search
    context.driver.find_element(*SEARCH_BUTTON).click()
    # wait for the page with search results to load
    sleep(6)

@then('Verify search worked')
def verify_search_results(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_text in actual_text, f'Expected {expected_text} ot in actual {actual_text}'


@then('Verify header in shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='utilityHeaderContainer']")

@then('Verify header has {number} links')
def verify_header_link_amount(context, number):
    number = int(number)  # convert str "6" ==> to int 6
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
    assert len(links) == number, f'Expected {number} links but got {len(links)}'

    # Make sure to always assert len() for multiple elements as shown above
    # because .find_elements() function never fails.
    # This code with incorrect locator will always pass:
    # context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav2613542']")

