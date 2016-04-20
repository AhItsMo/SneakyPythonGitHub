from PageObjectModels.HomeBeforeLoginPageObject import HomeBeforeLoginPageObject
from selenium.webdriver.common.keys import Keys

class HomeBeforeLoginMethods:

    def click_sign_in_button(self):
        #   Click the Sign In button on Home Page
        self.driver.find_element(*HomeBeforeLoginPageObject.sign_in_button).click()

    def use_search_box(self, search_string):
        #   Search for SneakyPythonGitHub using the Search Box on Home Page
        search_box = self.driver.find_element(*HomeBeforeLoginPageObject.search_box)
        search_box.clear()
        search_box.send_keys(search_string + Keys.RETURN)
