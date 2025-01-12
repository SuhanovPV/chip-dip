import allure
import pytest

from chip_dip.pages.main_page import MainPage


@allure.suite('Website')
@allure.parent_suite('Chip Dip services')
@allure.sub_suite('Search tests')
@allure.epic('Search')
@allure.story('Search product on site')
@pytest.mark.usefixtures('browser_settings')
class TestSearch:

    @allure.tag('web', 'search', 'product')
    @allure.title('Search existing product in cart')
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_results_found(self):
        search_text = 'ADS7846E'
        main_page = MainPage()
        main_page.open()
        main_page.search(search_text)
        main_page.should_found_result(search_text)

    @allure.tag('web', 'search', 'product')
    @allure.title('Search non-existent product in cart')
    @allure.severity(allure.severity_level.MINOR)
    def test_search_results_not_found(self):
        search_text = 'ыворваы'
        main_page = MainPage()
        main_page.open()
        main_page.search(search_text)
        main_page.should_not_found_result()
