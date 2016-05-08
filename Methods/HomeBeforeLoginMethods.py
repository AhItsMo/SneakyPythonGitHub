from PageObjectModels.HomeBeforeLoginPage import HomeBeforeLoginPage
from selenium.webdriver.common.keys import Keys

class HomeBeforeLoginMethods:

    #   Click the Sign In button on Home Page
    def click_sign_in_button(self):
        self.driver.find_element(*HomeBeforeLoginPage.sign_in_button).click()

    #   Search for SneakyPythonGitHub using the Search Box on Home Page
    def use_search_box(self, search_string):
        search_box = self.driver.find_element(*HomeBeforeLoginPage.search_box)
        search_box.clear()
        search_box.send_keys(search_string + Keys.RETURN)

    #   Verify that the Terms of Service link is displayed on the Home Page
    def terms_of_service_link_is_displayed(self):
        return self.driver.find_element(*HomeBeforeLoginPage.terms_of_service_link).is_displayed()
