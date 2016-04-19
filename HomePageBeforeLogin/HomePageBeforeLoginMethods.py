from HomePageBeforeLogin.HomePageBeforeLoginElements import HomePageElements

class HomePageMethods:

    def click_sign_in_button(self):
        #Click the Sign In button on Home Page
        self.driver.find_element(*HomePageElements.sign_in_button).click()
