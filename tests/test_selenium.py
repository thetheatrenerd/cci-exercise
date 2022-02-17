import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

def test_the_page():
    browser = webdriver.Chrome()
    
    browser.get("/index.html")
    bigBadButton = browser.find_element_by_id("clicky")
    mainText = browser.find_element_by_id("uh-oh").text
    newText = "YOU CLICKED THE BUTTON HOW COULD YOU"
    
    clicky.click()
    sleep(5)
    
    assert mainText == newText
    
    browser.close()

def dummy_test_1():
    num1 = 4
    num2 = 5
    num3 = 9

    sleep(27)

    assert num1 + num2 == num3

