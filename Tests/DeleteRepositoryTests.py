import unittest
from selenium.webdriver.common.by import By
from Utilities.BaseTestCase import BaseTestCase
from PageObjectModels import *


class MyTestCase(BaseTestCase):
    def test_01_delete_repository(self):
        repo_name = 'SneakyPythonTestRepo_8A1MOE'
        home_page = HomeAfterLoginPage.HomeAfterLoginPage(self.driver)

        home_page.open_repository(repo_name)

        repo_settings = RepositorySettingsPage.RepositorySettingsPage(self.driver)

        repo_settings.click_settings_link()

        repo_settings.click_delete_repository_button(repo_name)

        repo_settings.repository_is_deleted_successfully(self, repo_name)


if __name__ == '__main__':
    unittest.main()
