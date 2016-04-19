import unittest
from selenium import webdriver
from HomePageBeforeLogin.HomePageBeforeLoginElements import HomePageElements
from HomePageBeforeLogin.HomePageBeforeLoginMethods import HomePageMethods
from LoginPage.LoginPageElements import LoginPageElements


class HomePageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("https://github.com/")

#   Verify that clicking the Login button will navigate the user to the Login Page.
    def test_login_button(self):
#   Click Sign In button
        HomePageMethods.click_sign_in_button(self)

#       Assert that the Sign in to GitHub label is displayed
        self.assertTrue(self.driver.find_element(*LoginPageElements.sign_in_to_github_label).is_displayed())

#       Navigate back to the Home Page
        self.driver.get("https://github.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()
