import unittest
from PageObjectModels.LoginPage import LoginPage
from Utilities.BaseTestCase import BaseTestCase
from ddt import ddt, data, unpack


@ddt
class LoginTests(BaseTestCase):

    #   Verify that all Page Elements are loaded correctly
    def test_01_all_elements_are_loaded_correctly(self):
        login_page = LoginPage(self.driver)

        #   Verify that all Page Elements can be found
        login_page.validate_page_elements(login_page.page_elements_list)

    @data(*LoginPage.get_data_from_excel("LoginCredentials"))
    @unpack
    def test_02_sign_in(self, username, password, is_valid, comment):
        login_page = LoginPage(self.driver)

        #    Execute the Login Method using the data from the Excel sheet
        login_page.sign_in(username, password)

        #   Determine the outcome based on the validity of the credentials
        if is_valid:
            #   Assert that the Navigation Bar is displayed, which means that login is successful.
            login_page.is_profile_drop_down_displayed(self)
            #   Sign out, in order to continue testing from the start point (Login Page)
            login_page.sign_out()
            login_page.go_to_url(login_page.url)

        else:
            #   Assert that a Login error occurred by verifying that an error message is displayed.
            login_page.is_login_error_message_displayed(self)


if __name__ == '__main__':
    unittest.main()
