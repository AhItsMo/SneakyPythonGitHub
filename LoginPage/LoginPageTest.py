import unittest
from selenium import webdriver
from LoginPage import LoginPageMethods


class LoginPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("https://github.com/")

    def test_sign_in(self):
        LoginPageMethods.LoginPageMethod.sign_in_button(self, "dali@integrant.com", "123@sta.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
