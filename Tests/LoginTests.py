import unittest
from Utilities.BaseTestCase import BaseTestCase

from selenium import webdriver

from Methods.LoginMethods import LoginMethods
from Methods.NavigationBarMethods import NavigationBarMethods


class LoginTests(BaseTestCase):

    def test_sign_in(self):
#        Execute the Login Method, in order to log in as DinaAli
        LoginMethods.sign_in_button(self, "DinaAli", "123@sta.com")

#        Assert that the Navigation Bar is displayed, which means that login is successful.
        self.assertTrue(LoginMethods.is_profile_drop_down_displayed(self), "drop down menu is not displayed")

#        Sign out, in order to continue testing from the start point (Login Page)
        NavigationBarMethods.sign_out_list_item_click(self)
        self.driver.get("https://github.com/login")



if __name__ == '__main__':
    unittest.main()
