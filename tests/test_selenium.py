import unittest
from selenium import webdriver
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CheckThePage(unittest.TestCase):
    def click_and_check(self):

        try:
            self.driver.get('index.html')
            self.driver.maximize_window()
            self.driver.find_element_by_id('clicky').click()

            WebDriverWait(self.driver, 5)
            
            mainText = self.driver.find_element_by_id('uh-oh')

            newText = 'YOU CLICKED THE BUTTON HOW COULD YOU'
            self.assertEqual(mainText, newText)

            self.test_result = 'pass'

        except AssertionError as e:
            self.test_result = 'fail'
            raise

    def tearDown(self):
        print("Done with session %s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()