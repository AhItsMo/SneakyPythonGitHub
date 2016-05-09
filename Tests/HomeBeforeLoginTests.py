import unittest
from PageObjectModels.HomeBeforeLoginPage import HomeBeforeLoginPage
from PageObjectModels.LoginPage import LoginPage
from PageObjectModels.SearchResultsPage import SearchResultsPage
from PageObjectModels.TermsOfServicePage import TermsOfServicePage
from Utilities.BaseTestCase import BaseTestCase


class HomeBeforeLoginTests(BaseTestCase):

    #   Verify that all Page Elements are loaded correctly
    def test_01_all_elements_are_loaded_correctly(self):
        home_page = HomeBeforeLoginPage(self.driver)

        #   Verify that all Page Elements can be found
        home_page.validate_page_elements(home_page.page_elements_list)

    #   Verify that clicking the Login button will navigate the user to the Login Page.
    def test_02_click_login_button(self):
        home_page = HomeBeforeLoginPage(self.driver)

        #   Click Sign In button
        home_page.click_sign_in_button()

        #   Verify that the Login Page is loaded
        home_page.current_page_title_verification(self, LoginPage.title)

        #   Navigate back to the Home Page
        home_page.go_to_url(home_page.url)

    #  Verify that using the Search Box will navigate the user to the Search Results Page.
    def test_03_search_box(self):
        home_page = HomeBeforeLoginPage(self.driver)

        #   Search for "SneakyPythonGitHub" using the Home Page Search Box
        home_page.use_search_box("SneakyPythonGitHub")

        #   Verify that the Search Results Page is loaded.
        home_page.current_page_title_verification(self, SearchResultsPage.title)

        #   Navigate back to the Home Page
        home_page.go_to_url(home_page.url)

    #   Verify that clicking the Terms of Service link will navigate the user to the Terms of Service.
    def test_04_terms_of_service_link(self):
        home_page = HomeBeforeLoginPage(self.driver)

        #   Click the Terms of Service link
        home_page.click_terms_of_service_link()

        #   Switch to the new window that has just opened after clicking the Terms of Service Link
        home_page.switch_to_new_window()

        #   Verify that the Terms of Service Page is loaded in the new window
        home_page.current_page_title_verification(self, TermsOfServicePage.title)

        #   Close the new Window of the Terms Of Service
        home_page.close_and_switch_to_original_window()

if __name__ == '__main__':
    unittest.main(verbosity=2)
