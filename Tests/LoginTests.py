import unittest
from Utilities.BaseTestCase import BaseTestCase
from Methods.LoginMethods import LoginMethods
from Methods.NavigationBarMethods import NavigationBarMethods
from ddt import ddt, data, unpack



class LoginTests(BaseTestCase):
    @data(("path of excel sheet, name of sheet)
    @unpack
    def test_sign_in(self, username, password):
#        Execute the Login Method, in order to log in as DinaAli
        LoginMethods.sign_in_button(self, username, password)

#        Assert that the Navigation Bar is displayed, which means that login is successful.
        self.assertTrue(LoginMethods.is_profile_drop_down_displayed(self), "drop down menu is not displayed")

#        Sign out, in order to continue testing from the start point (Login Page)
        NavigationBarMethods.sign_out_list_item_click(self)
        self.driver.get("https://github.com/login")



if __name__ == '__main__':
    unittest.main()
