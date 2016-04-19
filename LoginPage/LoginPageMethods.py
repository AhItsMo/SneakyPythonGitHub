from loginPage.LoginPageElements import LoginPageElements


class LoginPageMethod:

    def sign_in_button(self, username, password):
        # Verify that clicking the Sign in button will navigate the user to the Home Page

        self.driver.find_element(*LoginPageElements.Username_box).send_keys(username)
        self.driver.find_element(*LoginPageElements.Password_box).send_keys(password)
        self.driver.find_element(*LoginPageElements.Sign_in_button).click()





