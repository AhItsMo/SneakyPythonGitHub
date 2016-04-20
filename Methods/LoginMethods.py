from PageObjectModels.LoginPageObject import LoginPageObject
from PageObjectModels.NavigationBarPageObject import NavigationBarPageObject


class LoginMethods:

    def sign_in_button(self, username, password):
        # Verify that clicking the Sign in button will navigate the user to the Home Page

        self.driver.find_element(*LoginPageObject.username_box).send_keys(username)
        self.driver.find_element(*LoginPageObject.password_box).send_keys(password)
        self.driver.find_element(*LoginPageObject.sign_in_button).click()

    def is_profile_drop_down_displayed(self):
        return self.driver.find_element(*NavigationBarPageObject.view_profile_drop_down).is_displayed()





