from abc import abstractmethod
from selenium.webdriver.common.by import By


class BasePage(object):
    #   Navigation Bar Locators
    view_profile_drop_down = (By.XPATH, "/html/body/div[2]/div/ul[2]/li[3]/a")
    sign_out_list_item = (By.XPATH, "/html/body/div[2]/div/ul[2]/li[3]/div/div/form/button")

    #   Properties
    @property
    def current_page_title(self):
        return self.driver.title

    #   Methods

    #   Initialization
    def __init__(self, driver):
        self.driver = driver

    #   Finding all Page Elements.
    def validate_page_elements(self, page_elements_list):
        try:
            for each_element in range(len(page_elements_list)):
                self.driver.find_element(*page_elements_list[each_element])

        except:
            raise InvalidPageException("The Page is not loaded. Current page title: " + self.driver.title)

    # Sign out from the current logged in user.
    def sign_out_list_item_click(self):
        self.driver.find_element(*self.view_profile_drop_down).click()
        self.driver.find_element(*self.sign_out_list_item).click()

    #   Verify that the current page title is correct

    #   Verify current page title
    def current_page_title_verification(self, current_page, expected_page_title):
        current_page.assertEqual(expected_page_title, self.driver.title,
                                 "The Expected Page is not loaded. Current page title is: " + self.driver.title)

    #   Navigate to URL
    def go_to_url(self, url):
        self.driver.get(url)


class InvalidPageException(Exception):
    #   Throw this exception when you don't find the correct page
    pass
