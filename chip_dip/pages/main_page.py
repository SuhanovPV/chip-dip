import allure
from selene import browser, have


class MainPage:
    @staticmethod
    def open():
        with allure.step('Open main page'):
            browser.open('/')

    @staticmethod
    def search(search_text: str):
        with allure.step(f'Serach product by test: "{search_text}"'):
            browser.element('#search__form [name=searchtext]').type(search_text)
            browser.element('#search__form [type=submit]').click()

    @staticmethod
    def should_found_result(search_text: str):
        with allure.step(f'Check products founded by text: {search_text}'):
            browser.all('#itemlist .name b').first.should(have.exact_text(search_text))

    @staticmethod
    def should_not_found_result():
        with allure.step(f'Check products not founded'):
            browser.element('#maybe').should(have.text("Товары не найдены"))

