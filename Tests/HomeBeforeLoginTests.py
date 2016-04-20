import unittest
from Utilities.BaseTestCase import BaseTestCase
from Methods.HomeBeforeLoginMethods import HomeBeforeLoginMethods
from PageObjectModels.LoginPageObject import LoginPageObject


class HomeTests(BaseTestCase):

    def test_login_button(self):
        #   Verify that clicking the Login button will navigate the user to the Login Page.

        #   Navigate to github.com
        self.driver.get("https://github.com/")

        #   Click Sign In button
        HomeBeforeLoginMethods.click_sign_in_button(self)

        #   Assert that the Sign in to GitHub label is displayed
        self.assertTrue(self.driver.find_element(*LoginPageObject.sign_in_to_github_label).is_displayed())

        #   Navigate back to the Home Page
        self.driver.get("https://github.com")


if __name__ == '__main__':
    unittest.main()
