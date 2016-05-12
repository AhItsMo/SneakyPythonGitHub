from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage
from PageObjectModels.HomeAfterLoginPage import HomeAfterLoginPage


class IntegrationPage(BasePage):

    #   Constants
    url = "https://github.com/"
    title = "https://github.com/integrations"

    #   Locators
    view_profile_drop_down = (By.CLASS_NAME, "header-nav-link name tooltipped tooltipped-sw js-menu-target")
    integration_view = (By.CLASS_NAME, "dropdown-item")
    integrations_directory_text = (By.LINK_TEXT, "Integrations Directory")
    your_dashboard_button = (By.CLASS_NAME, "btn site-header-actions-btn")


    page_elements_list = [view_profile_drop_down, integration_view, integrations_directory_text, your_dashboard_button]

    #   Methods

    #   Initialization
    def __init__(self, driver):
        super(HomeAfterLoginPage, self).__init__(driver)
        self.driver.get(self.url)
        self.pretest_login()

    #   Click on the Drop Down List on Home Page
    def click_view_profile_drop_list(self):
        self.driver.find_element(*self.view_profile_drop_down).click()

    #   Click the Integration Text on Drop Down List
    def click_integration_text(self):
        self.driver.find_element(*self.integration_text).click()

    #  Verify that Integrations Directory Link is displayed
    def integrations_directory_text_is_displayed(self):
        try:
            self.driver.find_element(*self.integration_text).is_displayed()
        except:
            print("Integrations Directory Link is not displayed")

    #   Click on the Your Dashboard Button
    def click_your_dashboard_button(self):
        self.driver.find_element(*self.your_dashboard_button).click()