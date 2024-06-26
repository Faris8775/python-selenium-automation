from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open Target.com website
driver.get('https://www.target.com/')

# click the SignIn button to invoke the Side Navigation
driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()

# wait for the SignIn sidebar to load
sleep(4)

# Click the SignIn on the side Navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']").click()

# Allow for the side navigation to load
sleep(4)

# Verify
expected_text = 'Sign into your Target account'
actual_text = driver.find_element(By.XPATH, "//h1[.//span]").text
# print(actual_text)
assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

print('Test case passed')