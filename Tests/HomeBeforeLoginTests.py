import unittest
from Utilities.BaseTestCase import BaseTestCase
from Methods.HomeBeforeLoginMethods import HomeBeforeLoginMethods
from PageObjectModels.LoginPageObject import LoginPageObject
from PageObjectModels.SearchResultsPageObject import SearchResultsPageObject


class HomeTests(BaseTestCase):

    #   Verify that clicking the Login button will navigate the user to the Login Page.
    def test_login_button(self):

        self.driver.get("https://github.com/")
        #   Navigate to github.com

        HomeBeforeLoginMethods.click_sign_in_button(self)
        #   Click Sign In button

        self.assertTrue(self.driver.find_element(*LoginPageObject.sign_in_to_github_label).is_displayed())
        #   Assert that the Sign in to GitHub label is displayed

        self.driver.get("https://github.com")
        #   Navigate back to the Home Page

    #  Verify that entering a text in the search box and pressing Enter will navigate the user to the
    #  Search Results Page.
    def test_search_box(self):

        self.driver.get("https://github.com")
        #   Navigate to github.com

        HomeBeforeLoginMethods.use_search_box(self, "SneakyPythonGitHub")
        #   Search for the string "SneakyPythonGitHub"

        search_label = self.driver.find_element(*SearchResultsPageObject.search_label)
        self.assertEqual(search_label.text, "Search", "Search Label is not displayed correctly")
        #   Verify that Search Label is displayed on the Search Results page

        repo_name = self.driver.find_element(*SearchResultsPageObject.repo_name_link).text
        self.assertEqual(repo_name, "AhItsMo/SneakyPythonGitHub", "Repository Name is not displayed correctly")
        #   Verify that the Repository Link is displayed on the Search Results page


if __name__ == '__main__':
    unittest.main()
