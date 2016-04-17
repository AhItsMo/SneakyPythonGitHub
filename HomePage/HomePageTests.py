import unittest
from selenium import webdriver
from HomePage.HomePageElements import HomePageElements
from LoginPage.LoginPageElements import LoginPageElements


class HomePageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("https://github.com/")

    def test_login_button(self):
        #Verify that clicking the Login button will navigate the user to the Login Page.
        self.driver.find_element(*HomePageElements.login_button).click()


    @classmethod
    def tearDownClass(cls):

if __name__ == '__main__':
    unittest.main()
