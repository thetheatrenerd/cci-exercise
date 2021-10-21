from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)
driver.get('/index.html')

# Click the button
big_bad_button = driver.find_element_by_id('clicky')
big_bad_button.click()

