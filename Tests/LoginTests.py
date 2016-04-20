import unittest

from selenium import webdriver

from Methods.LoginMethods import LoginMethods
from Methods.NavigationBarMethods import NavigationBarMethods


class LoginTests(unittest.TestCase):
    # def setUp(self):
    #     self.driver = webdriver.Firefox()
    #     self.driver.implicitly_wait(30)
    #     self.driver.maximize_window()
    #     self.driver.get("https://github.com/login")

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("https://github.com/login")

    def test_sign_in(self):
#        Execute the Login Method, in order to log in as DinaAli
        LoginMethods.sign_in_button(self, "DinaAli", "123@sta.com")

#        Assert that the Navigation Bar is displayed, which means that login is successful.
        self.assertTrue(LoginMethods.is_profile_drop_down_displayed(self), "drop down menu is not displayed")

#        Sign out, in order to continue testing from the start point (Login Page)
        NavigationBarMethods.sign_out_list_item_click(self)
        self.driver.get("https://github.com/login")

        # @classmethod
        #  def tearDownClass(cls):
        #      cls.driver.quit()

        # def tearDown(self):
        #     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
