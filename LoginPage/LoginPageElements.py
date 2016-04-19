from selenium.webdriver.common.by import By


class LoginPageElements:

    Home_icon = (By.XPATH, "/html/body/div[2]/div/a")
    Username_box = (By.ID, "login_field")
    Password_box = (By.ID, "password")
    Sign_in_button = (By.XPATH, "/html/body/div[4]/div[1]/div/form/div[4]/input[2]")
    sign_in_to_github_label = (By.XPATH, "/html/body/div[4]/div[1]/div/form/div[2]/h1")