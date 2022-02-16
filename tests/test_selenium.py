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

def dummy_test_1():
    num1 = 4
    num2 = 5
    num3 = 9

    assert num1 + num2 == num3

def dummy_test_2():
    num1 = 27
    num2 = 27

    assert num1 == num2


def dummy_test_3():
    num1 = 2
    num2 = 3

    assert num1 + num2 == num2 + num1

