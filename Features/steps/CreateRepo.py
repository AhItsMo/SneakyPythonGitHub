import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.join(sys.path[0], os.pardir), os.pardir)))
from behave import *
from PageObjectModels import *
from Utilities.TestData import NewRepository
from Utilities.BaseTestCase import BaseTestCase


@given('a repository is being created')
def step_impl(context):
    home_page = HomeBeforeLoginPage.HomeBeforeLoginPage(context.browser)
    home_page.pretest_login()

    home_page = HomeAfterLoginPage.HomeAfterLoginPage(context.browser)
    home_page.click_new_repository_button()


@when('the user attempts to use an unavailable repository name')
def step_impl(context):
    create_page = CreateNewRepositoryPage.CreateNewRepositoryPage(context.browser)
    create_page.create_new_repository(NewRepository['Name'], NewRepository['Description'])


@then('the repository already exists error message appears')
def step_impl(context):
    create_page = CreateNewRepositoryPage.CreateNewRepositoryPage(context.browser)
    assert create_page.repository_already_exists_error_is_displayed() is True


@when('the user attempts to use an available repository name')
def step_impl(context):
    create_page = CreateNewRepositoryPage.CreateNewRepositoryPage(context.browser)
    repo_id = create_page.id_generator()
    create_page.create_new_repository(NewRepository['Name'] + '_' + repo_id, NewRepository['Description'] +
                                      " Repository ID: " + repo_id)


@then('the repository is created successfully')
def step_impl(context):
    repo_code_page = RepositoryCodePage.RepositoryCodePage(context.browser)
    current_test = BaseTestCase()
    repo_code_page.current_page_title_verification(current_test, repo_code_page.title)

