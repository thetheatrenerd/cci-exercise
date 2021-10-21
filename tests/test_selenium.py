import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

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