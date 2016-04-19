from LoginPage.LoginPageElements import LoginPageElements


class LoginPageMethods:

    def sign_in_button(self, username, password):
        # Verify that clicking the Sign in button will navigate the user to the Home Page

        self.driver.find_element(*LoginPageElements.username_box).send_keys(username)
        self.driver.find_element(*LoginPageElements.password_box).send_keys(password)
        self.driver.find_element(*LoginPageElements.sign_in_button).click()





