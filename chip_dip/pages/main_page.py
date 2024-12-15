from selene import browser, have


class MainPage:
    @staticmethod
    def open():
        browser.open('/')

    @staticmethod
    def search(search_text: str):
        browser.element('#search__form [name=searchtext]').type(search_text)
        browser.element('#search__form [type=submit]').click()

    @staticmethod
    def should_found_result(search_text: str):
        browser.all('#itemlist .name b').first.should(have.exact_text(search_text))

    @staticmethod
    def should_not_found_result():
        browser.element('#maybe').should(have.text("Товары не найдены"))

