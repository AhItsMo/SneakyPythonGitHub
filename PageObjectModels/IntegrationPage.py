from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage
from PageObjectModels.HomeAfterLoginPage import HomeAfterLoginPage


class IntegrationPage(BasePage):

    #   Constants
    url = "https://github.com/integrations"
    title = "Integrations Directory"

    #   Locators
    integrations_directory_text = (By.LINK_TEXT, "Integrations Directory")
    your_dashboard_button = (By.XPATH, "html/body/header/div/div/div/a")

    page_elements_list = [integrations_directory_text, your_dashboard_button]

    #   Methods

    #   Initialization
    def __init__(self, driver):
        super(IntegrationPage, self).__init__(driver)
        self.pretest_login()
        self.driver.get(self.url)

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