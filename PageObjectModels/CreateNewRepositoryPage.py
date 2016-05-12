from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Utilities.BasePage import BasePage


class CreateNewRepositoryPage(BasePage):
    #   Constants
    url = "https://github.com/new"
    title = "Create a New Repository"

    #   Locators

    page_elements_list = []

    #   Methods

    #   Initialization
    def __init__(self, driver):
        super(CreateNewRepositoryPage, self).__init__(driver)
        self.driver.get(self.url)

