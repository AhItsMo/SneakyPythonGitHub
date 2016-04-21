from PageObjectModels.LoginPageObject import LoginPageObject
from PageObjectModels.NavigationBarPageObject import NavigationBarPageObject


class LoginMethods:

    # Verify that clicking the Sign in button will navigate the user to the Home Page
    def sign_in_button(self, username, password):

        self.driver.find_element(*LoginPageObject.username_box).send_keys(username)
        self.driver.find_element(*LoginPageObject.password_box).send_keys(password)
        self.driver.find_element(*LoginPageObject.sign_in_button).click()

    # Verify that clicking the forget password button will navigate the user to the Reset your password Page
    def forget_password_text(self):
        self.driver.find_element(*LoginPageObject.forget_password).click()

    #   Return whether the Profile Drop down is displayed
    def is_profile_drop_down_displayed(self):
        return self.driver.find_element(*NavigationBarPageObject.view_profile_drop_down).is_displayed()

    #   Return whether the Sign in to GitHub label is displayed
    def sign_in_to_github_label_is_displayed(self):
        return self.driver.find_element(*LoginPageObject.sign_in_to_github_label).is_displayed()





