from selenium.webdriver.common.by import By


class SearchResultsPageObject:
    search_label = (By.CSS_SELECTOR, "div.container:nth-child(1) > h1:nth-child(1)")

    search_box = (By.XPATH, ".//*[@id='search_form']/div[2]/div[1]/input[1]")

    repo_name_link = (By.XPATH, ".//*[@id='container']/div[2]/div/div[2]/ul/li/h3/a")
