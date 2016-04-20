from PageObjectModels.NavigationBarPageObject import NavigationBarPageObject


class NavigationBarMethods:

    #  Verify that clicking the profile drop down list and sign out list item will navigate the user to the Home Page
    def sign_out_list_item_click(self):

        self.driver.find_element(*NavigationBarPageObject.view_profile_drop_down).click()
        self.driver.find_element(*NavigationBarPageObject.sign_out_list_item).click()
