from selenium.webdriver.common.by import By


class TermsOfServicePage:
    #   Constants
    url = "https://help.github.com/articles/github-terms-of-service/"
    title = "GitHub Terms of Service - User Documentation"

    #   Locators
    github_terms_of_service_label = (By.XPATH, "html/body/div[1]/div[2]/div/div[2]/h2")
