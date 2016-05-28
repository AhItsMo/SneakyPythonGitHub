import time
import unittest

from ddt import ddt, data, unpack

from PageObjectModels.IntegrationPage import IntegrationPage
from Utilities.BaseTestCase import BaseTestCase


@ddt
class IntegrationTests(BaseTestCase):

    #   Verify that all Page Elements are loaded correctly
    def test_01_all_elements_are_loaded_correctly(self):
        integration_page = IntegrationPage(self.driver)

        #   Verify that all Page Elements can be found
        integration_page.validate_page_elements(self, integration_page.page_elements_list)

    # Verify integrations directory text is displayed
        integration_page.integrations_directory_text_is_displayed()

    @data(*IntegrationPage.get_data_from_excel("FilterIntegration"))
    @unpack
    def test_02_use_filter_integration_search_box(self, search_string, isvalid):
        integration_page = IntegrationPage(self.driver)

        #    Execute the Filter Method using the data from the Excel sheet
        integration_page.use_filter_integration_search_box(search_string)
        time.sleep(3)

        if isvalid:
            # Assert that there are results displayed
            self.assertTrue(integration_page.is_results_displayed(), "No results are displayed")
        else:
            # Assert that there are no results displayed
            self.assertFalse(integration_page.is_results_displayed(), "Results displayed for invalid search")




if __name__ == '__main__':
    unittest.main()


