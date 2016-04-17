from selenium.webdriver.common.by import By


class HomePageElements:

        home_icon = (By.XPATH, "/html/body/header/div/a")

        search_box = (By.XPATH, "/html/body/header/div/div/div/a[1]")

        login_button = (By.XPATH, "/html/body/header/div/div/div/a[2]")

        sign_up_button = (By.XPATH, "/html/body/header/div/div/div/a[1]")

        pick_a_username_box = (By.XPATH, "/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/dl[1]/dd/input")

        your_email_address_box = (By.XPATH, "/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/dl[2]/dd/input")

        sign_up_for_github_button = (By.XPATH, "/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/button")

        terms_of_service_link = (By.XPATH, "/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/p/a[1]")

        privacy_policy_link = (By.XPATH, "/html/body/div[4]/div[1]/div/div/div[2]/div[1]/form/p/a[2]")

        sign_up_for_github_button_2 = (By.XPATH, "/html/body/div[4]/div[4]/div/div/div[1]/a")
