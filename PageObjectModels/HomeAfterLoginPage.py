from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Utilities.BasePage import BasePage
from PageObjectModels.LoginPage import LoginPage


class HomeAfterLoginPage(BasePage):
    #   Constants
    url = "https://github.com"
    title = "GitHub"

    #   Locators
    learn_git_and_github_label = (By.CLASS_NAME, "shelf-title")
    using_the_hello_world_guide_label = (By.CLASS_NAME, "shelf-lead")
    lets_get_started_button = (By.CSS_SELECTOR, "a.btn:nth-child(3)")
    dash_board_dropdown = (By.CSS_SELECTOR, "button.btn")
    new_repository_button = (By.CLASS_NAME, "boxed-group-action")

    page_elements_list = [learn_git_and_github_label, using_the_hello_world_guide_label, lets_get_started_button,
                          dash_board_dropdown, new_repository_button]

    #   Methods

    #   Initialization
    def __init__(self, driver):
        super(HomeAfterLoginPage, self).__init__(driver)
        self.driver.get(self.url)
        self.pretest_login()

    #   Click Let's get started! button
    def click_lets_get_started_button(self):
        self.driver.find_element(*self.lets_get_started_button).click()

    #   Click New Repository Button
    def click_new_repository_button(self):
        self.driver.find_element(*self.new_repository_button).click()
