import unittest
from selenium import webdriver


class BaseClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get("https://github.com")

    def tearDown(self):
        self.driver.close()
