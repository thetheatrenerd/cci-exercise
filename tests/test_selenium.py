from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

browser = webdriver.Chrome()
browser.get("/index.html")
bigBadButton = browser.find_element_by_id("clicky")
mainText = browser.find_element_by_id("uh-oh").text
newText = "YOU CLICKED THE BUTTON HOW COULD YOU"
clicky.click()
sleep(5)
assert mainText == newText
browser.close()