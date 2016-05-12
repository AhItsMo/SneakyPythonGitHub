import xlrd
from selenium.webdriver.common.by import By


# noinspection PyBroadException
class BasePage(object):
    #   Navigation Bar Locators
    view_profile_drop_down = (By.XPATH, "/html/body/div[2]/div/ul[2]/li[3]/a")
    sign_out_list_item = (By.XPATH, "/html/body/div[2]/div/ul[2]/li[3]/div/div/form/button")
    username_box = (By.ID, "login_field")
    password_box = (By.ID, "password")
    sign_in_button = (By.XPATH, "/html/body/div[4]/div[1]/div/form/div[4]/input[3]")
    create_new_dropdown = (By.CSS_SELECTOR, "#user-links > li:nth-child(2) > a > svg > path")
    new_repository_list_item = (By.CSS_SELECTOR, "#user-links > li.header-nav-item.dropdown.js-menu-container.active > "
                                                 "div > ul > a:nth-child(1)")

    #   Properties

    #   Methods

    #   Initialization
    def __init__(self, driver):
        self.driver = driver

    #   Finding all Page Elements.
    def validate_page_elements(self, current_test, page_elements_list):
        #   Create a list to capture all validation errors and continue Test Case execution.
        from selenium.common.exceptions import NoSuchElementException
        validation_errors = []

        for each_element in range(len(page_elements_list)):
            #   Try to find the element. No exception will occur if the element exists
            try:
                self.driver.find_element(*page_elements_list[each_element])

            # The element is not found and "No Such Element Exception" is raised
            except NoSuchElementException:
                #   Print the missing element in the output report
                print("The following element is missing: " +
                      str(page_elements_list[each_element]) + ". Current page title: " + self.driver.title)

                #   Append a string to the "Validation Errors" list.
                validation_errors.append("No Such Element Exception. Element #" + str(each_element + 1))

        # Assert that the "Validation Errors" list is empty, to determine if the Test Case passed or failed.
        current_test.assertEqual([], validation_errors)

    # Sign out from the current logged in user.
    def sign_out(self):
        self.driver.find_element(*self.view_profile_drop_down).click()
        self.driver.find_element(*self.sign_out_list_item).click()

    #   Verify current page title
    def current_page_title_verification(self, current_page, expected_page_title):
        current_page.assertRegex(self.driver.title, expected_page_title,
                                 "The Expected Page is not loaded. Current page title is: " + self.driver.title)

    #   Navigate to URL
    def go_to_url(self, url):
        self.driver.get(url)

    #   Switch to the new window that has just opened
    def switch_to_new_window(self):
        self.driver.switch_to_window(self.driver.window_handles[-1])

    #   Close the new window (currently open) and switch to original window
    def close_and_switch_to_original_window(self):
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    #   Create a New Repository from the "Create new" drop-down list
    def open_create_new_dropdown(self):
        self.driver.find_element(*self.create_new_dropdown).click()
        self.driver.find_element(*self.new_repository_list_item).click()

    #   Pre-test conditional login (if the user is not already logged in)
    def pretest_login(self):
        try:
            self.driver.find_element(*self.view_profile_drop_down).is_displayed()
        except:
            print("User is not logged in. Pre-test login is executed")
            self.driver.get("https://github.com/login")
            self.driver.find_element(*self.username_box).send_keys("sneakypythontestuser")
            self.driver.find_element(*self.password_box).send_keys("000000aa")
            self.driver.find_element(*self.sign_in_button).click()

    # read data from a certain sheet in the Test Data workbook "SneakyPythonGitHubTestData.xlsx"
    @staticmethod
    def get_data_from_excel(sheet_name):
        # create an empty ist to get data
        rows = []
        # open excel workbook and get excel sheet
        book = xlrd.open_workbook('..\Tests\SneakyPythonGitHubTestData.xlsx')
        sheet = book.sheet_by_name(sheet_name)
        for row_index in range(1, sheet.nrows):
            rows.append(list(sheet.row_values(row_index, 0, sheet.ncols)))
        return rows


class InvalidPageException(Exception):
    #   Throw this exception when you don't find the correct page
    pass
