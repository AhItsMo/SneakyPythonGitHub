import unittest
from selenium import webdriver
import os


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chromedriver = (os.path.dirname(os.getcwd()) + "/Utilities/chromedriver")
        os.environ["webdriver.chrome.driver"] = chromedriver
        cls.driver = webdriver.Chrome(chromedriver)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
