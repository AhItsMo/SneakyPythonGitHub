import unittest

from PageObjectModels import HomeAfterLoginPage, HelloWorldGitHubPage, CreateNewRepositoryPage
from Utilities.BaseTestCase import BaseTestCase


class HomeAfterLoginTests(BaseTestCase):
    #   Verify that all Page Elements are loaded correctly
    def test_01_all_elements_are_loaded_correctly(self):
        home_page = HomeAfterLoginPage.HomeAfterLoginPage(self.driver)

        #   Verify that all Page Elements can be found
        home_page.validate_page_elements(self, home_page.page_elements_list)

    #   Verify that pressing Let's get started! button will navigate the user to Hello World GitHub guide
    def test_02_lets_get_started_button(self):
        home_page = HomeAfterLoginPage.HomeAfterLoginPage(self.driver)

        #   Click Let's get started! button
        home_page.click_lets_get_started_button()

        #   Switch to the new window that has just opened after clicking the button
        home_page.switch_to_new_window()

        #   Verify that the Hello World GitHub guide Page is loaded
        home_page.current_page_title_verification(self, HelloWorldGitHubPage.HelloWorldGitHubPage.title)

        #   Close the new Window of World GitHub guide
        home_page.close_and_switch_to_original_window()

    #   Verify that selecting the New Repository list item in Create New drop-down list navigates to Create New Repo.
    def test_03_select_create_new_repository_from_create_new_dropdown(self):
        home_page = HomeAfterLoginPage.HomeAfterLoginPage(self.driver)

        #   Click Create New list, then select New Repository list item
        home_page.open_create_new_dropdown()

        #   Verify the current page title
        home_page.current_page_title_verification(self, CreateNewRepositoryPage.CreateNewRepositoryPage.title)


if __name__ == '__main__':
    unittest.main()
