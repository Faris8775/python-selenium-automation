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

# open the url
driver.get('https://www.amazon.com/')

# Amazon Logo, by tag.class
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

# Create Account, by tag.class
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# Your Name text area, ID
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# Mobile number or email text area, ID
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# Password text area , ID
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# Password must be at least 6 characters and icon, by tag.class
driver.find_element(By.CSS_SELECTOR, "div.a-box.a-alert-inline.a-alert-inline-info.auth-inlined-information-message.a-spacing-top-min")

# Re-enter Password Authenticator, ID
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# Continue button, ID
driver.find_element(By.CSS_SELECTOR,"#continue")

# Legal text
driver.find_element(By.CSS_SELECTOR, "#legalTextRow")

# Conditions of use, by tag and attribute
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

# Privacy notice, by tab and attribute
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

# Sign in, by class
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")



