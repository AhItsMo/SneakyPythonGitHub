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
    repositories_list = (By.ID, "repo_listing")

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

    #   Open repository
    def open_repository(self, repository_name):
        selected_repository = (By.PARTIAL_LINK_TEXT, repository_name)
        self.driver.find_element(*selected_repository).click()

    #   Get the name of the first repository on the Repositories list
    def get_first_repository_name(self):
        repository_listing = self.driver.find_element(*self.repositories_list)
        first_repository_listing = repository_listing.find_element(By.CLASS_NAME, "repo")
        return first_repository_listing.get_attribute('innerHTML')

