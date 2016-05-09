from PageObjectModels.SearchResultsPage import SearchResultsPage

class SearchResultsMethods:

    #   Verify that Search Label is displayed on the Search Results page
    def search_label_text_is_displayed_correctly(self):
        search_label = self.driver.find_element(*SearchResultsPage.search_label)
        self.assertEqual(search_label.text, "Search", "Search Label is not displayed correctly")
