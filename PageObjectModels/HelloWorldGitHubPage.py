from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Utilities.BasePage import BasePage
from PageObjectModels.LoginPage import LoginPage


class HelloWorldGitHubPage(BasePage):
    #   Constants
    url = "https://guides.github.com/activities/hello-world/"
    title = "Hello World · GitHub Guides"
