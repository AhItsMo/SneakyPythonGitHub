import unittest
from selenium import webdriver


class BaseClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get("https://github.com")

        login_button = self.driver.find_element_by_xpath("/html/body/header/div/div/div/a[2]")

        sign_up_button = self.driver.find_element_by_xpath("/html/body/header/div/div/div/a[1]")

        search_box = self.driver.find_element_by_xpath("/html/body/header/div/div/div/a[1]")

        pick_a_username_box = self.driver.find_element_by_xpath\
            ("/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/dl[1]/dd/input")

        your_email_address_box = self.driver.find_element_by_xpath\
            ("/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/dl[2]/dd/input")

        sign_up_for_github_button = self.driver.find_element_by_xpath\
            ("/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/button")

        terms_of_service_link = self.driver.find_element_by_xpath\
            ("/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/p/a[1]")

        privacy_policy_link = self.driver.find_element_by_xpath\
            ("/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/p/a[2]")

        sign_up_for_github_button_2 = self.driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div[1]/a")

    def tearDown(self):
        self.driver.close()
