import unittest
from selenium import webdriver
from NavigationBar.NavigationBarElements import NavigationBarElements
from NavigationBar.NavigationBarMethods import NavigationBarMethods
from LoginPage.LoginPageMethods import LoginPageMethods


class LoginPageTest(unittest.TestCase):
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
        LoginPageMethods.sign_in_button(self, "DinaAli", "123@sta.com")

#        Assert that the Navigation Bar is displayed, which means that login is successful.
        self.assertTrue(self.driver.find_element(*NavigationBarElements.view_profile_drop_down).is_displayed())

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
