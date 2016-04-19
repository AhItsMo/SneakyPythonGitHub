from selenium.webdriver.common.by import By


class LoginPageElements:

    home_icon = (By.XPATH, "/html/body/div[2]/div/a")
    username_box = (By.id, "login_field")
    password_box = (By.id, "password")
    sign_in_button = (By.XPATH, "/html/body/div[4]/div[1]/div/form/div[4]/input[2]")





