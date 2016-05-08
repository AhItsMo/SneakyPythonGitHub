from PageObjectModels.TermsOfServicePageObject import TermsOfServicePageObject


class TermsOfServiceMethods:

    #   Switch to the new window that has just opened after clicking the Terms of Service Link
    def switch_to_terms_of_service_browser_window(self):
        original_window_handle = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[-1])
        return original_window_handle

    #   Verify that the Terms of Service Page is displayed in another window
    def terms_of_service_page_is_displayed(self):
        #   Verify that the Page Title is displayed correctly
        self.assertEqual(self.driver.title, "GitHub Terms of Service - User Documentation",
                         "GitHub Terms of Service Page is not loaded. Incorrect page title: " + self.driver.title)

    #   Close the new window of the Terms Of Service page.
    def close_terms_of_service_browser_window(self, original_window_handle):
        self.driver.close()
        self.driver.switch_to_window(original_window_handle)
