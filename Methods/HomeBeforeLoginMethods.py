from PageObjectModels.HomeBeforeLoginPageObject import HomeBeforeLoginPageObject
from selenium.webdriver.common.keys import Keys

class HomeBeforeLoginMethods:

    #   Click the Sign In button on Home Page
    def click_sign_in_button(self):
        self.driver.find_element(*HomeBeforeLoginPageObject.sign_in_button).click()

    #   Search for SneakyPythonGitHub using the Search Box on Home Page
    def use_search_box(self, search_string):
        search_box = self.driver.find_element(*HomeBeforeLoginPageObject.search_box)
        search_box.clear()
        search_box.send_keys(search_string + Keys.RETURN)


