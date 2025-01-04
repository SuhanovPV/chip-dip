from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from chip_dip.app_pages.main_page import MainPage


class CartPage:
    @staticmethod
    def is_cart_empty():
        product = browser.all((AppiumBy.ID, 'ru.chipdip.mobile:id/item_cart_content_container'))
        return len(product) == 0

    def should_product_be_in_cart(self, name):
        browser.element(
            (AppiumBy.ID, 'ru.chipdip.mobile:id/item_cart_product_name_label_text_view')
        ).should(have.text(name))
        return self

    def clear_cart(self):
        browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/textView_delete_selected_items')).click()
        return self

    def clear_cart_if_not_empty(self):
        main_page = MainPage()
        main_page.open_page_via_side_menu('main_cart_button')
        if not self.is_cart_empty():
            self.clear_cart()
        return self

    def should_cart_be_empty(self):
        browser.element(
            (AppiumBy.ID, 'ru.chipdip.mobile:id/common_error_content_label_text_view')
        ).should(have.exact_text('Ваша корзина пока пуста.'))
        return self