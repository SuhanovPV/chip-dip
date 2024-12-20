import allure
from selene import browser, have


class CartPage:
    @staticmethod
    def open():
        with allure.step('Open cart page'):
            browser.open('/cart')

    @staticmethod
    def should_present_products(products: dict):
        with allure.step(f'Check products {list(products.keys())} in cart'):
            browser.all('.cart__item .name').should(have.texts(*[x for x in products.keys()]))


    @staticmethod
    def clear():
        with allure.step('Delete all products'):
            browser.element('#delete_checked').click()
        with allure.step('Confirm deletion'):
            browser.element('#fancyConfirm_ok').click()

    @staticmethod
    def order_goods():
        with allure.step('Go to order page'):
            browser.element('#cart_form [type="submit"]').click()

    @staticmethod
    def should_be_empty():
        with allure.step('Check cart is empty'):
            browser.element('#cart_empty h3' ).should(have.exact_text('Сейчас в корзине нет товаров'))

    def clear_if_not_empty(self):
        with allure.step('Clear cart if not empty'):
            self.open()
            cart_lit = browser.all('#cart_itemlist tr')
            if len(cart_lit) > 1:
                self.clear()

