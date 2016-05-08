from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Utilities.BasePage import BasePage


class HomeBeforeLoginPage(BasePage):

    #   Locators
    home_icon = (By.XPATH, "/html/body/header/div/a")
    search_box = (By.XPATH, "html/body/header/div/div/nav[2]/div/form/label/input")
    sign_in_button = (By.XPATH, "/html/body/header/div/div/div/a[2]")
    sign_up_button = (By.XPATH, "/html/body/header/div/div/div/a[1]")
    pick_a_username_box = (By.XPATH, "/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/dl[1]/dd/input")
    your_email_address_box = (By.XPATH, "/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/dl[2]/dd/input")
    create_a_password_box = (By.XPATH, "/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/dl[3]/dd/input")
    sign_up_for_github_button = (By.XPATH, "/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/button")
    terms_of_service_link = (By.XPATH, "/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/p/a[1]")
    privacy_policy_link = (By.XPATH, "/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/p/a[2]")
    sign_up_for_github_button_2 = (By.XPATH, "/html/body/div[4]/div[4]/div/div/div[1]/a")
    welcome_home_developers_label = (By.XPATH, "/html/body/div[4]/div[2]/div[1]/h2")

    page_elements_list = [home_icon, search_box, sign_in_button, sign_up_button, pick_a_username_box,
                          your_email_address_box, create_a_password_box, sign_up_for_github_button,
                          terms_of_service_link, privacy_policy_link, sign_up_for_github_button_2,
                          welcome_home_developers_label]

    url = "https://github.com"

    #   Methods

    #   Initialization
    def __init__(self, driver):
        super(HomeBeforeLoginPage, self).__init__(driver)
        self.driver.get("https://github.com/")

    #   Click the Sign In button on Home Page
    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    #   Search for SneakyPythonGitHub using the Search Box on Home Page
    def use_search_box(self, search_string):
        search_box = self.driver.find_element(*self.search_box)
        search_box.clear()
        search_box.send_keys(search_string + Keys.RETURN)

    #   Verify that the Terms of Service link is displayed on the Home Page
    def terms_of_service_link_is_displayed(self):
        return self.driver.find_element(*self.terms_of_service_link).is_displayed()
