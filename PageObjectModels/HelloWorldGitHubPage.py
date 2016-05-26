from Utilities.BasePage import BasePage


class HelloWorldGitHubPage(BasePage):
    #   Constants
    url = "https://guides.github.com/activities/hello-world/"
    title = "Hello World · GitHub Guides"

    #   Locators

    page_elements_list = []

    #   Methods

    #   Initialization
    def __init__(self, driver):
        super(HelloWorldGitHubPage, self).__init__(driver)
        self.driver.get(self.url)
