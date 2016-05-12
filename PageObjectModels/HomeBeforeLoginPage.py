from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Utilities.BasePage import BasePage


class HomeBeforeLoginPage(BasePage):
    #   Constants
    url = "https://github.com"
    title = "How people build software · GitHub"

    #   Locators
    home_icon = (By.CSS_SELECTOR, "body > header > div > a > svg")
    search_box = (By.NAME, "q")
    sign_in_button = (By.CSS_SELECTOR, "body > header > div > div > div > a.btn.site-header-actions-btn.mr-2")
    sign_up_button = (By.CSS_SELECTOR, "body > header > div > div > div > a.btn.btn-primary.site-header-actions-btn")
    pick_a_username_box = (By.NAME, "user[login]")
    your_email_address_box = (By.NAME, "user[email]")
    create_a_password_box = (By.NAME, "user[password]")
    sign_up_for_github_button = (By.XPATH, "/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/button")
    terms_of_service_link = (By.LINK_TEXT, "terms of service")
    privacy_policy_link = (By.LINK_TEXT, "privacy policy")
    sign_up_for_github_button_2 = (By.XPATH, "html/body/div[4]/div[5]/div/div/div[1]/a")
    welcome_home_developers_label = (By.XPATH, "html/body/div[4]/div[3]/div[1]/h2")

    page_elements_list = [home_icon, search_box, sign_in_button, sign_up_button, pick_a_username_box,
                          your_email_address_box, create_a_password_box, sign_up_for_github_button,
                          terms_of_service_link, privacy_policy_link,
                          sign_up_for_github_button_2, welcome_home_developers_label]

    #   Methods

    #   Initialization
    def __init__(self, driver):
        super(HomeBeforeLoginPage, self).__init__(driver)
        self.driver.get(self.url)

    #   Click the Sign In button on Home Page
    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    #   Search for SneakyPythonGitHub using the Search Box on Home Page
    def use_search_box(self, search_string):
        search_box = self.driver.find_element(*self.search_box)
        search_box.clear()
        search_box.send_keys(search_string + Keys.RETURN)

    #   Click Terms of Service link
    def click_terms_of_service_link(self):
        self.driver.find_element(*self.terms_of_service_link).click()
