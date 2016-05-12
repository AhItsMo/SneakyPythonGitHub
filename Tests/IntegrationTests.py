import unittest
from PageObjectModels.HomeAfterLoginPage import HomeAfterLoginPage
from Utilities.BaseTestCase import BaseTestCase
from PageObjectModels.IntegrationPage import IntegrationPage
from Utilities.BasePage import BasePage


class IntegrationPage(BaseTestCase):

        #   Verify that all Page Elements are loaded correctly
       def test_01_all_elements_are_loaded_correctly(self):
              home_page = HomeAfterLoginPage.HomeAfterLoginPage(self.driver)

        #   Verify that all Page Elements can be found
        #home_page.validate_page_elements(home_page.page_elements_list)

        #   Click Let's get started! button
        IntegrationPage.click_view_profile_drop_list()

        #  Click Let's get started! button
        IntegrationPage.click_integration_text()

        #   Verify integrations directory text is displayed
        IntegrationPage.integrations_directory_text_is_displayed()

        #    Click on the Your Dashboard Button
        IntegrationPage.click_your_dashboard_button()


if __name__ == '__main__':
    unittest.main()
