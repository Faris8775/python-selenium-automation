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

# Amazon Logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

# Email Field
driver.find_element(By.ID, 'ap_email')

# Continue Button
driver.find_element(By.ID, 'continue')

# Conditions of use link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Conditions of Use']")

# Privacy Notice link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Privacy Notice']")

# Need Help link
driver.find_element(By.XPATH,"//span[@text()='Need help?']")

# Shop Amazon Business
driver.find_element(By.XPATH,"//span[@text()='Shop on Amazon Business']")


# Create your Amazon account button
driver.find_element(By.ID,'createAccountSubmit')
