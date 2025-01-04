from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class CatalogPage:
    def search_product_in_catalog(self, name):
        browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/search_bar_input_edit_text')).click()
        browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/search_bar_input_edit_text')).type(name)
        browser.all(
            (AppiumBy.ID, 'ru.chipdip.mobile:id/item_catalog_text_label_text_view')
        ).first.should(have.text(name))
        return self

    def back_to_catalog_from_search(self):
        browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/search_bar_left_image_view')).click()
        return self

    def add_founded_product_to_cart(self):
        browser.all((AppiumBy.ID, 'ru.chipdip.mobile:id/progress_button_text_view')).first.click()
        browser.all(
            (AppiumBy.ID, 'ru.chipdip.mobile:id/progress_button_text_view')
        ).first.should(have.exact_text('В корзине'))
        return self