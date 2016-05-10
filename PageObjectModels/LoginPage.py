from Utilities.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    #   Constants
    url = "https://github.com/login"
    title = "Sign in to GitHub · GitHub"

    #   Locators
    home_icon = (By.XPATH, "/html/body/div[2]/div/a")
    username_box = (By.ID, "login_field")
    password_box = (By.ID, "password")
    sign_in_button = (By.XPATH, "/html/body/div[4]/div[1]/div/form/div[4]/input[3]")
    sign_in_to_github_label = (By.XPATH, "/html/body/div[4]/div[1]/div/form/div[2]/h1")
    forgot_password_link = (By.CLASS_NAME, "label-link")
    incorrect_username_or_password_label = (By.XPATH, ".//*[@id='js-flash-container']/div/div")

    page_elements_list = [home_icon, username_box, password_box, sign_in_button, sign_in_to_github_label,
                          forgot_password_link]

    #   Methods

    #   Initialization
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.driver.get(self.url)

    #   Sign in.
    def sign_in(self, username, password):
        self.driver.find_element(*self.username_box).send_keys(username)
        self.driver.find_element(*self.password_box).send_keys(password)
        self.driver.find_element(*self.sign_in_button).click()

    #   Verify that clicking the forget password button will navigate the user to the Reset your password Page
    def forget_password_text(self):
        self.driver.find_element(*self.forgot_password_link).click()

    #   Return whether the Profile Drop down is displayed
    def is_profile_drop_down_displayed(self, current_page):
        current_page.assertTrue(self.driver.find_element(*self.view_profile_drop_down).is_displayed())

    #   Asserts that a login error occurred by verifying that an error message is displayed
    def is_login_error_message_displayed(self, current_page):
        current_page.assertTrue(self.driver.find_element(*self.incorrect_username_or_password_label).is_displayed())

    #   Return whether the Sign in to GitHub label is displayed
    def sign_in_to_github_label_is_displayed(self):
        return self.driver.find_element(*LoginPage.sign_in_to_github_label).is_displayed()
