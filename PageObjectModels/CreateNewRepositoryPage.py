from selenium.webdriver.common.by import By

from Utilities.BasePage import BasePage


class CreateNewRepositoryPage(BasePage):
    #   Constants
    url = "https://github.com/new"
    title = "Create a New Repository"

    #   Locators
    repository_name_box = (By.ID, "repository_name")
    repository_description_box = (By.ID, "repository_description")
    create_repository_button = (By.CSS_SELECTOR, "#new_repository > div.with-permission-fields > button")
    repository_already_exists_error = (By.CLASS_NAME, 'error')

    page_elements_list = [repository_name_box, repository_description_box, create_repository_button]

    #   Methods

    #   Initialization
    def __init__(self, driver):
        super(CreateNewRepositoryPage, self).__init__(driver)
        self.pretest_login()
        if self.driver.current_url != self.url and self.driver.current_url != 'https://github.com/repositories':
            self.driver.get(self.url)

    #   Create a new repository using a given name and description
    def create_new_repository(self, name, description):
        self.driver.find_element(*self.repository_name_box).send_keys(name)
        self.driver.find_element(*self.repository_description_box).send_keys(description)
        self.driver.find_element(*self.create_repository_button).click()

    #   Asserts that the "Repository Already Exists" error message is displayed
    def repository_already_exists_error_is_displayed(self):
        return self.driver.find_element(*self.repository_already_exists_error).is_displayed()
