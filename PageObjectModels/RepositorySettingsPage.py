from selenium.webdriver.common.by import By

from Utilities.BasePage import BasePage


class RepositorySettingsPage(BasePage):
    #   Constants
    url = "https://github.com/"
    title = "SneakyPythonTestUser.*"

    #   Locators
    settings_link = (By.XPATH, '//*[@id="js-repo-pjax-container"]/div[1]/div[2]/nav/a[4]')
    delete_this_repository_button = (By.CSS_SELECTOR, '#options_bucket > div.boxed-group.dangerzone >'
                                                      ' div > button:nth-child(11)')
    repository_name_to_confirm_deletion_box = (By.CSS_SELECTOR, '#facebox > div > div > form > p > input')
    i_understand_the_consequences_button = (By.CSS_SELECTOR, '#facebox > div > div > form > button')
    repository_is_deleted_label = (By.XPATH, '//*[@id="js-flash-container"]/div/div')

    page_elements_list = [settings_link]

    #   Methods

    #   Initialization
    def __init__(self, driver):
        super(RepositorySettingsPage, self).__init__(driver)

    #   Click Settings Link
    def click_settings_link(self):
        self.driver.find_element(*self.settings_link).click()

    #   Delete the opened repository by clicking the Delete button and verifying the repository name
    def delete_opened_repository(self, repository_name):
        self.driver.find_element(*self.delete_this_repository_button).click()
        self.driver.find_element(*self.repository_name_to_confirm_deletion_box).send_keys(repository_name)
        self.driver.find_element(*self.i_understand_the_consequences_button).click()

    #   Verify that the repository deletion is completed successfully
    def repository_is_deleted_successfully(self, current_test, repository_name):
        deletion_confirmation_message = self.driver.find_element(*self.repository_is_deleted_label).text
        current_test.assertEqual('Your repository "SneakyPythonTestUser/' + repository_name +
                                 '" was successfully deleted.', deletion_confirmation_message)

    #   Click the Delete Repository button
    def click_delete_repository_button(self):
        self.driver.find_element(*self.delete_this_repository_button).click()

    #   Verify the name of the repository being deleted
    def verify_repository_name_being_deleted(self, repository_name):
        self.driver.find_element(*self.repository_name_to_confirm_deletion_box).send_keys(repository_name)
        self.driver.find_element(*self.i_understand_the_consequences_button).click()
