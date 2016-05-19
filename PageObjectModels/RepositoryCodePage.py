from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage


class RepositoryCodePage(BasePage):
    #   Constants
    url = "https://github.com/"
    title = "SneakyPythonTestUser.*"

    #   Locators
    code_link = (By.CSS_SELECTOR, '#js-repo-pjax-container > div.pagehead.repohead.instapaper_'
                                  'ignore.readability-menu.experiment-repo-nav > div:nth-child(2) > nav > '
                                  'span:nth-child(1) > a')

    page_elements_list = [code_link]

    #   Methods

    #   Initialization
    def __init__(self, driver):
        super(RepositoryCodePage, self).__init__(driver)
