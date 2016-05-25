from behave import *

from PageObjectModels.HomeAfterLoginPage import HomeAfterLoginPage
from PageObjectModels.RepositorySettingsPage import RepositorySettingsPage
from Utilities.BaseTestCase import BaseTestCase

repo_name = ''


@given('Repository Settings page is displayed')
def step_impl1(context):
    #   Get the name of the first repository on the repositories list and open it.
    home_page = HomeAfterLoginPage(context.browser)
    global repo_name
    repo_name = home_page.get_first_repository_name()
    home_page.open_repository(repo_name)
    repo_settings_page = RepositorySettingsPage(context.browser)
    repo_settings_page.click_settings_link()


@when('the user attempts to delete this repository')
def step_impl(context):
    #   Attempt to delete the opened repository
    repo_settings_page = RepositorySettingsPage(context.browser)
    repo_settings_page.click_delete_repository_button()


@when('the user verifies the name of the repository being deleted')
def step_impl(context):
    #   The user verifies the name of the repository being deleted
    repo_settings_page = RepositorySettingsPage(context.browser)
    repo_settings_page.verify_repository_name_being_deleted(repo_name)


@then('the repository is deleted successfully')
def step_impl(context):
    #   Verify that a message is displayed; saying that the repository is deleted successfully
    repo_settings_page = RepositorySettingsPage(context.browser)
    current_test = BaseTestCase()
    repo_settings_page.repository_is_deleted_successfully(current_test, repo_name)
