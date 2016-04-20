from PageObjectModels.HomeBeforeLoginPageObject import HomeBeforeLoginPageObject

class HomeBeforeLoginMethods:

    def click_sign_in_button(self):
        #Click the Sign In button on Home Page
        self.driver.find_element(*HomeBeforeLoginPageObject.sign_in_button).click()
