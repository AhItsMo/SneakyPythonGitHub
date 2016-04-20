import unittest
from Utilities.BaseTestCase import BaseTestCase
from Methods.HomeBeforeLoginMethods import HomeBeforeLoginMethods
from Methods.LoginMethods import LoginMethods
from Methods.SearchResultsMethods import SearchResultsMethods
from PageObjectModels.HomeBeforeLoginPageObject import HomeBeforeLoginPageObject
from PageObjectModels.TermsOfServicePageObject import TermsOfServicePageObject


class HomeTests(BaseTestCase):

    #   Verify that clicking the Login button will navigate the user to the Login Page.
    def test_login_button(self):

        #   Navigate to github.com
        self.driver.get("https://github.com/")

        #   Click Sign In button
        HomeBeforeLoginMethods.click_sign_in_button(self)

        #   Assert that the Sign in to GitHub label is displayed
        self.assertTrue(LoginMethods.sign_in_to_github_label_is_displayed(self))

        #   Navigate back to the Home Page
        self.driver.get("https://github.com")

    #  Verify that entering a text in the search box and pressing Enter will navigate the user to the
    #  Search Results Page.
    def test_search_box(self):

        #   Navigate to github.com
        self.driver.get("https://github.com")

        #   Search for the string "SneakyPythonGitHub"
        HomeBeforeLoginMethods.use_search_box(self, "SneakyPythonGitHub")

        #   Verify that Search Label is displayed on the Search Results page
        SearchResultsMethods.search_label_text_is_displayed_correctly(self)

        #   Navigate back to the Home Page
        self.driver.get("https://github.com")

    #   Verify that clicking the Terms of Service link will navigate the user to the Terms of Service.
    def test_terms_of_service_link(self):
        #   Navigate to github.com
        self.driver.get("https://github.com/")

        #   Assert that the Terms of Service link is displayed
        self.assertTrue(self.driver.find_element(*HomeBeforeLoginPageObject.terms_of_service_link).is_displayed())

        #   Click the Terms of Service link
        self.driver.find_element(*HomeBeforeLoginPageObject.terms_of_service_link).click()


        self.driver.switch_to_window(self.driver.window_handles[-1])
        github_terms_of_service_label = self.driver.find_element\
            (*TermsOfServicePageObject.github_terms_of_service_label)
        self.assertEqual(github_terms_of_service_label.text, "GitHub Terms of Service",
                         "GitHub Terms of Service Label is not displayed correctly")
        #

        #   Navigate back to the Home Page
        self.driver.get("https://github.com")


if __name__ == '__main__':
    unittest.main()
