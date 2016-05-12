import unittest
from PageObjectModels.HomeAfterLoginPage import HomeAfterLoginPage
from Utilities.BaseTestCase import BaseTestCase
from PageObjectModels.IntegrationPage import IntegrationPage
from Utilities.BasePage import BasePage


class IntegrationTests(BaseTestCase):

    #   Verify that all Page Elements are loaded correctly
    def test_01_all_elements_are_loaded_correctly(self):
        integration_page = IntegrationPage(self.driver)

        #   Verify that all Page Elements can be found
        integration_page.validate_page_elements(self, integration_page.page_elements_list)

    #def test_02_


if __name__ == '__main__':
    unittest.main()



    # #   Click Let's get started! button
    # IntegrationPage.click_view_profile_drop_list()
    #
    # #  Click Let's get started! button
    # IntegrationPage.click_integration_text()
    #
    # #   Verify integrations directory text is displayed
    # IntegrationPage.integrations_directory_text_is_displayed()
    #
    # #    Click on the Your Dashboard Button
    # IntegrationPage.click_your_dashboard_button()
