from LoginPage.LoginPageElements import LoginPageElements
from NavigationBar.NavigationBarElements import NavigationBarElements

class LoginPageMethods:

    def sign_in_button(self, username, password):
        # Verify that clicking the Sign in button will navigate the user to the Home Page

        self.driver.find_element(*LoginPageElements.username_box).send_keys(username)
        self.driver.find_element(*LoginPageElements.password_box).send_keys(password)
        self.driver.find_element(*LoginPageElements.sign_in_button).click()

    def is_profile_drop_down_displayed(self):
        return self.driver.find_element(*NavigationBarElements.view_profile_drop_down).is_displayed()





