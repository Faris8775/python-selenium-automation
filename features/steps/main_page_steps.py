from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

# CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
# SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")


@given('Open target main page')
def open_target(context):
    context.app.main_page.open()

@when('Click Target Circle page')
def open_target_circle(context):
    context.app.header.open_target_circle()


@when('Search for {product}')
def search_product(context, product):
    print('Step layer:', product)
    context.app.header.search_product(product)

@when('Click on Cart icon')
def click_cart_icon(context):
    # context.driver.wait.until(EC.element_to_be_clickable(*CART_ICON)).click()
    context.app.header.click_cart()



@when('Click Sign In')
def main_sign_in(context):
    # click the sign in on main page
    # context.driver.wait.until(EC.element_to_be_clickable(MAIN_SIGN_IN)).click()
    # wait for the SignIn sidebar to load
    # sleep(2)
    context.app.header.main_sign_in()


@when('From right side navigation menu, click Sign In')
def side_sign_in(context):
    # click the side nav sign in
    # context.driver.wait.until(EC.element_to_be_clickable(SIDE_SIGN_IN)).click()
    # wait for the SignIn sidebar to load
    # sleep(4)
    context.app.header.side_sign_in()


# @when('Search for {product}')
# def search_product(context, product):
#     # find search field and enter text
#     # context.driver.find_element(By.ID, 'search').send_keys(product)
#     # click search
#     # context.driver.find_element(*SEARCH_BUTTON).click()
#     # wait for the page with search results to load
#     # sleep(6)
#     context.app.header.search_product(product)

@then('Verify search worked')
def verify_search_results(context):
    expected_text = 'product'
    # actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    # assert expected_text in actual_text, f'Expected {expected_text} ot in actual {actual_text}'
    context.app.search_results_page.verify_search_results(expected_text)


@then('Verify header in shown')
def verify_header_present(context):
    context.app.main_page.verify_header_present()

@then('Verify header has {number} links')
def verify_header_link_amount(context, number):
    context.app.header.verify_header_link_amount(number)


@then('Verify can click every link')
def verify_click_links(context):
    context.app.header.verify_click_links()

