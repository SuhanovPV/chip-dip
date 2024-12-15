from chip_dip.pages.main_page import MainPage


class TestCart:
    def test_search_results_found(self):
        search_text = 'ADS7846E'
        main_page = MainPage()
        main_page.open()
        main_page.search(search_text)
        main_page.should_found_result(search_text)

    def test_search_results_not_found(self):
        search_text = 'ыворваы'
        main_page = MainPage()
        main_page.open()
        main_page.search(search_text)
        main_page.should_not_found_result()
