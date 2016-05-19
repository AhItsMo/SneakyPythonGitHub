import unittest
from Utilities.BaseTestCase import BaseTestCase
from PageObjectModels import *
from PageObjectModels.CreateNewRepositoryPage import CreateNewRepositoryPage
from PageObjectModels.RepositoryCodePage import RepositoryCodePage
from Utilities.TestData import NewRepository


class CreateRepositoryTests(BaseTestCase):
    def test_01_all_elements_are_loaded_correctly(self):
        create_page = CreateNewRepositoryPage.CreateNewRepositoryPage(self.driver)

        create_page.validate_page_elements(self, create_page.page_elements_list)

    def test_02_create_repository_fail(self):
        create_page = CreateNewRepositoryPage(self.driver)

        create_page.create_new_repository(NewRepository['Name'] + " new", NewRepository['Description'] + "new")

        create_page = CreateNewRepositoryPage(self.driver)
        error_message = create_page.repository_already_exists_error_is_displayed()
        self.assertTrue(error_message)

    def test_03_create_repository_success(self):
        create_page = CreateNewRepositoryPage(self.driver)

        repo_id = create_page.id_generator()
        create_page.create_new_repository(NewRepository['Name'] + '_' + repo_id, NewRepository['Description'] +
                                          " Repository ID: " + repo_id)

        repo_code_page = RepositoryCodePage(self.driver)
        current_test = BaseTestCase()
        repo_code_page.current_page_title_verification(current_test, repo_code_page.title)


if __name__ == '__main__':
    unittest.main()
