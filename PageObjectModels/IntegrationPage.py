from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Utilities.BasePage import BasePage


class IntegrationPage(BasePage):

    #   Constants
    url = "https://github.com/integrations"
    title = "Integrations Directory"

    #   Locators
    integrations_directory_text = (By.LINK_TEXT, "Integrations Directory")
    filter_integrations_search_box = (By.ID, "integration-filter-field")
    tools_displayed = (By.CLASS_NAME,"intgrs-lstng-item-link")

    page_elements_list = [integrations_directory_text, filter_integrations_search_box]

    #   Methods

    #   Initialization
    def __init__(self, driver):
        super(IntegrationPage, self).__init__(driver)
        self.driver.get(self.url)

    #  Verify that Integrations Directory Link is displayed
    def integrations_directory_text_is_displayed(self):
        try:
            self.driver.find_element(*self.integrations_directory_text).is_displayed()
            assert "Integrations Directory" in self.driver.find_element(*self.integrations_directory_text).text
        except:
            print("Integrations Directory Link is not displayed")

    #   Search for string using the Filter Integration Box
    def use_filter_integration_search_box(self, search_string):
        self.driver.find_element(*self.filter_integrations_search_box).send_keys(search_string)


    def is_results_displayed(self):
        try:
            list_of_element = self.driver.find_elements(*self.tools_displayed)
            list_of_displayed_element = []
            for i in range (0, len(list_of_element)):
                if list_of_element[i].is_displayed():
                    list_of_displayed_element.append(list_of_element[i])
                    print(list_of_element[i])

            if len(list_of_displayed_element) > 0:
                print("Number of found elements is: " + str(len(list_of_displayed_element)))
                return True

        except NoSuchElementException:
            return False



