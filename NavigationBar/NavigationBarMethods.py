from NavigationBar.NavigationBarElements import NavigationBarElements


class NavigationBarMethods:

    def sign_out_list_item_click(self):
        # Verify that clicking the Sign in button will navigate the user to the Home Page

        self.driver.find_element(*NavigationBarElements.view_profile_drop_down).click()
        self.driver.find_element(*NavigationBarElements.sign_out_list_item).click()
